import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
INSERT INTO users (username, password)
VALUES ('codealpha', 'codealpha123')
""")

conn.commit()
conn.close()

print("Database Created Successfully!")