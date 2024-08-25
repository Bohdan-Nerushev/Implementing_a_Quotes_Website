"""
URL configuration for quotes_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# C:\Users\Lenovo\Desktop\Home_Work_10\quotes_site\quotes_site\urls.py


from django.urls import path
from quotes.views import signup, login_view, quotes_list, author_detail, logout, new_quote, add_author

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('quotes/', quotes_list, name='quotes_list'),  # Список всіх цитат
    path('quotes/page/<int:page>/', quotes_list, name='quotes_list_page'),  # Пагінація (змінив URL для логічного порядку)
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('logout/', logout, name='logout'),
    path('new-quote/', new_quote, name='new_quote'),  # Додавання цитати (URL змінив на "new-quote" для більш звичного формату)
    path('add-author/', add_author, name='add_author'),  # Додавання автора (URL змінив на "add-author")
    path('', quotes_list, name='quote_list'),  # Головна сторінка (на "quotes_list" змінив на відповідний до інших)
]
