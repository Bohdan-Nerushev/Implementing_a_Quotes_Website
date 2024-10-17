# quotes/models.py
from django.db import models

# C:\Users\Lenovo\Desktop\Home_Work_10\quotes_site\quotes\models.py

from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.fullname

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.quote[:50]  # Повертає перші 50 символів цитати




class QuoteTag(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
