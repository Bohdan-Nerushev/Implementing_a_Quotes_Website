import os
import django
import json
from django.db import transaction

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_site.settings')
django.setup()

from quotes.models import Author, Tag, Quote

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def import_data():
    try:
        authors_path = os.path.join(BASE_DIR, 'authors.json')
        with open(authors_path, 'r', encoding='utf-8') as f:
            authors = json.load(f)
    except FileNotFoundError:
        print(f"File {authors_path} not found.")
        return

    try:
        quotes_path = os.path.join(BASE_DIR, 'qoutes.json')
        with open(quotes_path, 'r', encoding='utf-8') as f:
            quotes = json.load(f)
    except FileNotFoundError:
        print(f"File {quotes_path} not found.")
        return

    with transaction.atomic():
        for author_data in authors:
            Author.objects.get_or_create(
                fullname=author_data['fullname'],
                defaults={
                    'born_date': author_data.get('born_date') or None,
                    'born_location': author_data.get('born_location') or '',
                    'description': author_data.get('description') or ''
                }
            )

        for quote_data in quotes:
            author = Author.objects.filter(fullname=quote_data['author']).first()
            if author:
                quote_obj, created = Quote.objects.get_or_create(
                    quote=quote_data['quote'],
                    author=author
                )
                for tag_name in quote_data['tags']:
                    tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                    quote_obj.tags.add(tag_obj)

if __name__ == '__main__':
    import_data()
    print("Data successfully imported into the database.")
