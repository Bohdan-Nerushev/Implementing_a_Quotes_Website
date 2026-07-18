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
