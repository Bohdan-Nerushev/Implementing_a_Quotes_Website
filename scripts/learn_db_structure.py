import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Get schema of each table
for table_name in tables:
    print(f"Table: {table_name[0]}")
    cursor.execute(f"PRAGMA table_info({table_name[0]});")
    columns = cursor.fetchall()
    for column in columns:
        print(f"  Column: {column[1]}, Type: {column[2]}, Not Null: {column[3]}, Default: {column[4]}")
    print()

# Close connection
conn.close()
