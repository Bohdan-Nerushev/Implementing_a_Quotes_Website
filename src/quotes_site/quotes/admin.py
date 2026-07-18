from django.contrib import admin
from .models import Author, Tag, Quote

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'born_date', 'born_location')
    search_fields = ('fullname', 'born_location')
    list_filter = ('born_date',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('get_excerpt', 'author')
    list_filter = ('author', 'tags')
    search_fields = ('quote',)

    def get_excerpt(self, obj):
        return obj.quote[:50] + '...' if len(obj.quote) > 50 else obj.quote
    get_excerpt.short_description = 'Quote'

