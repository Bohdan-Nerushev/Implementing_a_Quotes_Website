from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Tag, Quote

class QuotesSiteTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            fullname="Test Author",
            born_date="1980-01-01",
            born_location="Test City",
            description="Test biography"
        )
        self.tag = Tag.objects.create(name="test")
        self.quote = Quote.objects.create(
            quote="This is a test quote.",
            author=self.author
        )
        self.quote.tags.add(self.tag)
        
        self.username = "testuser"
        self.password = "SecurePassword123"
        self.email = "testuser@example.com"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email
        )

    def test_quotes_list_view(self):
        response = self.client.get(reverse('quotes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a test quote.")
        self.assertContains(response, "Test Author")

    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Author")
        self.assertContains(response, "Test biography")

    def test_signup_view_get(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_post_success(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'Password123!',
            'password_confirm': 'Password123!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
        new_user = User.objects.get(username='newuser')
        self.assertTrue(new_user.check_password('Password123!'))

    def test_login_view_success(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)

    def test_login_view_failure(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'WrongPassword123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password.")

    def test_logout_view_get_forbidden(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 405)

    def test_logout_view_post_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_new_quote_requires_login(self):
        response = self.client.get(reverse('new_quote'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_add_author_requires_login(self):
        response = self.client.get(reverse('add_author'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_new_quote_post_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('new_quote'), {
            'quote': 'Another test quote.',
            'author': self.author.id,
            'tags': [self.tag.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Quote.objects.filter(quote='Another test quote.').exists())

    def test_add_author_post_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('add_author'), {
            'fullname': 'New Author',
            'born_date': '1990-05-15',
            'born_location': 'New City',
            'description': 'Bio description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Author.objects.filter(fullname='New Author').exists())

    def test_signup_view_post_failed(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'Password123!',
            'password_confirm': 'WrongPassword123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registration failed. Please correct the errors below.")

    def test_signup_view_post_weak_password(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': '123',
            'password_confirm': '123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registration failed. Please correct the errors below.")

    def test_profile_view_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_profile_view_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username)

    def test_change_password_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('change_password'), {
            'old_password': self.password,
            'new_password1': 'NewSecurePassword123!',
            'new_password2': 'NewSecurePassword123!'
        })
        self.assertEqual(response.status_code, 302)
        # Verify password changed
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('NewSecurePassword123!'))

    def test_delete_account_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('delete_account'), {
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username=self.username).exists())

    def test_delete_account_wrong_password(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('delete_account'), {
            'password': 'WrongPassword123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username=self.username).exists())
        self.assertContains(response, "Incorrect password. Please try again.")

    def test_change_email_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('change_email'), {
            'email': 'newemail@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'newemail@example.com')

    def test_change_email_already_exists(self):
        # Create another user with the target email
        User.objects.create_user(username='otheruser', password='Password123!', email='taken@example.com')
        
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('change_email'), {
            'email': 'taken@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This email is already in use by another account.")
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.email, 'taken@example.com')

    def test_add_tag_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('add_tag'), {
            'name': 'Inspiration'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name='inspiration').exists())

    def test_add_tag_already_exists(self):
        Tag.objects.create(name='inspiration')
        
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('add_tag'), {
            'name': 'Inspiration'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This tag already exists.")



