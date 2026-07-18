import logging
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm, RegisterForm, AuthorForm
from .models import Quote, Author
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

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
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


