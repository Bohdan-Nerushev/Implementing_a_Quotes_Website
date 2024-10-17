import sqlite3
import json

# Підключення до бази даних
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Завантаження даних з JSON-файлів
with open('authors.json', 'r', encoding='utf-8') as f:
    authors = json.load(f)

with open('qoutes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

# Вставка даних у таблицю quotes_author
for author in authors:
    cursor.execute("""
        INSERT INTO quotes_author (fullname, born_date, born_location, description)
        VALUES (?, ?, ?, ?)
    """, (author['fullname'], author['born_date'], author['born_location'], author['description']))

# Вставка даних у таблицю quotes_quote та отримання id авторів
author_ids = {}
cursor.execute("SELECT id, fullname FROM quotes_author")
for row in cursor.fetchall():
    author_ids[row[1]] = row[0]

for quote in quotes:
    author_id = author_ids.get(quote['author'])
    if author_id is not None:
        cursor.execute("""
            INSERT INTO quotes_quote (quote, author_id)
            VALUES (?, ?)
        """, (quote['quote'], author_id))

        # Вставка тегів у таблицю quotes_tag, якщо їх немає
        for tag in quote['tags']:
            cursor.execute("""
                INSERT OR IGNORE INTO quotes_tag (name)
                VALUES (?)
            """, (tag,))

        # Отримання id тегів
        tag_ids = {}
        cursor.execute("SELECT id, name FROM quotes_tag")
        for row in cursor.fetchall():
            tag_ids[row[1]] = row[0]

        # Вставка зв'язків між цитатами та тегами
        cursor.execute("SELECT id FROM quotes_quote WHERE quote = ?", (quote['quote'],))
        quote_id = cursor.fetchone()[0]

        for tag in quote['tags']:
            tag_id = tag_ids.get(tag)
            if tag_id is not None:
                cursor.execute("""
                    INSERT INTO quotes_quotetag (quote_id, tag_id)
                    VALUES (?, ?)
                """, (quote_id, tag_id))

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()

print("Дані успішно імпортовані у базу даних.")

