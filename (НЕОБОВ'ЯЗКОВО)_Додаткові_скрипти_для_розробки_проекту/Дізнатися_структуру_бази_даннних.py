import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Отримання списку таблиць
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Отримання схеми кожної таблиці
for table_name in tables:
    print(f"Table: {table_name[0]}")
    cursor.execute(f"PRAGMA table_info({table_name[0]});")
    columns = cursor.fetchall()
    for column in columns:
        print(f"  Column: {column[1]}, Type: {column[2]}, Not Null: {column[3]}, Default: {column[4]}")
    print()

# Закриття з'єднання
conn.close()
