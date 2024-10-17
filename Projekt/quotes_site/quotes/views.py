from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Імпортуємо messages для відображення повідомлень
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm, RegisterForm, AuthorForm
from .models import Quote, Author
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
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
            return redirect('quotes_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('quotes_list')

def quotes_list(request):
    page_number = request.GET.get('page', 1)
    quotes = Quote.objects.all().order_by('-id')
    paginator = Paginator(quotes, 5)
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotes/quotes_list.html', {'page_obj': page_obj})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})

@login_required(login_url='login')  # Додаємо login_url, щоб перенаправляти користувачів на сторінку входу
def new_quote(request):
    if not request.user.is_authenticated:  # Перевірка аутентифікації користувача
        messages.info(request, 'Please register or log in to add a quote.')
        return redirect('login')
    
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes_list')
    else:
        form = QuoteForm()
    return render(request, 'quotes/new_quote.html', {'form': form})

@login_required(login_url='login')  # Додаємо login_url
def add_author(request):
    if not request.user.is_authenticated:  # Перевірка аутентифікації користувача
        messages.info(request, 'Please register or log in to add an author.')
        return redirect('login')
    
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes_list')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

