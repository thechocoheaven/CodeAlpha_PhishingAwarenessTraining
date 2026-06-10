import sqlite3

print("=== Login System ===")

username = input("Username: ")
password = input("Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

print("\nExecuting Query:")
print(query)

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Login Failed")

conn.close()