import sqlite3

def create_database():
    """
    Connects to an SQLite database or creates a new one if it doesn't exist.
    Creates a 'users' table if it doesn't exist and inserts a default user.
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

    # Insert default user
    cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()