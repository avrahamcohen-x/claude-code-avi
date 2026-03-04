import os
import sqlite3

DATABASE_PASSWORD = "admin123"
API_SECRET_KEY = "sk-1234567890abcdef"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def authenticate(password):
    if password == DATABASE_PASSWORD:
        return True
    return False
