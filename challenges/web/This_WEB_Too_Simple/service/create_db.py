import sqlite3
import hashlib

def create_database():
    """
    Connects to an SQLite database or creates a new one if it doesn't exist.
    Creates a 'users' table if it doesn't exist and inserts a default user with a hashed password.
    """
    # Database file name
    db_filename = 'database.db'

    # Connect to the SQLite database. If it doesn't exist, it will be created.
    conn = sqlite3.connect(db_filename)

    # Create a cursor object using the cursor method
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    # Static username
    username = 'user'

    # Hash the static password
    password = 'user123'
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert default user with hashed password
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
