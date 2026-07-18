import logging
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm, RegisterForm, AuthorForm, DeleteAccountForm, EmailChangeForm, TagForm
from .models import Quote, Author, Tag
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

logger = logging.getLogger('quotes')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            logger.info("User registered and logged in successfully: %s", user.username)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('quotes_list')
        else:
            logger.warning("Failed registration attempt")
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            logger.info("User logged in successfully: %s", user.username)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('quotes_list')
        else:
            logger.warning("Failed login attempt")
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@require_POST
def logout(request):
    username = request.user.username
    auth_logout(request)
    logger.info("User logged out: %s", username)
    messages.info(request, "You have been logged out.")
    return redirect('quotes_list')

def quotes_list(request):
    page_number = request.GET.get('page', 1)
    quotes = Quote.objects.all().order_by('-id')
    paginator = Paginator(quotes, 5)
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotes_list.html', {'page_obj': page_obj})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author_detail.html', {'author': author})

@login_required(login_url='login')
def new_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            logger.info("New quote ID %d added by user %s", quote.id, request.user.username)
            messages.success(request, "Quote added successfully!")
            return redirect('quotes_list')
        else:
            logger.warning("Failed quote addition attempt by user %s", request.user.username)
            messages.error(request, "Failed to add quote. Please correct the errors below.")
    else:
        form = QuoteForm()
    return render(request, 'new_quote.html', {'form': form})

@login_required(login_url='login')
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            logger.info("New author '%s' added by user %s", author.fullname, request.user.username)
            messages.success(request, "Author added successfully!")
            return redirect('quotes_list')
        else:
            logger.warning("Failed author addition attempt by user %s", request.user.username)
            messages.error(request, "Failed to add author. Please correct the errors below.")
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


@login_required(login_url='login')
def profile_view(request):
    return render(request, 'profile.html')


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logger.info("Password changed successfully for user: %s", request.user.username)
            messages.success(request, "Your password was successfully updated!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors in the password form.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST, user=request.user)
        if form.is_valid():
            user = request.user
            username = user.username
            user.delete()
            logger.info("User account deleted: %s", username)
            messages.success(request, "Your account has been deleted successfully.")
            return redirect('quotes_list')
        else:
            messages.error(request, "Please enter your correct password to delete your account.")
    else:
        form = DeleteAccountForm(user=request.user)
    return render(request, 'delete_account.html', {'form': form})


@login_required(login_url='login')
def change_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            logger.info("Email updated successfully for user: %s", request.user.username)
            messages.success(request, "Your email address has been successfully updated!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors in the email form.")
    else:
        form = EmailChangeForm(instance=request.user)
    return render(request, 'change_email.html', {'form': form})


@login_required(login_url='login')
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            logger.info("New tag '%s' added by user %s", tag.name, request.user.username)
            messages.success(request, "Tag added successfully!")
            return redirect('quotes_list')
        else:
            logger.warning("Failed tag addition attempt by user %s", request.user.username)
            messages.error(request, "Failed to add tag. Please correct the errors below.")
    else:
        form = TagForm()
    return render(request, 'add_tag.html', {'form': form})





