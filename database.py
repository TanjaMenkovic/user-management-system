import sqlite3
from typing import Optional, Dict

DB_NAME: str = "user_management.db"

def initialize_database() -> None:
    """
    Initializes the SQLite database by creating the users table if it doesn't already exist.
    """
    conn: sqlite3.Connection = sqlite3.connect(DB_NAME)
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            password_salt TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user(username: str, email: str, password_data: Dict[str, str]) -> bool:
    """
    Adds a new user to the database.
    :param username: The unique username for the user.
    :param email: The user's email address.
    :param password_data: A dictionary containing the hashed password and salt.
    :return: True if the user is added successfully, False if the username already exists.
    """
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_NAME)
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password_hash, password_salt)
            VALUES (?, ?, ?, ?)
        """, (username, email, password_data["hash"], password_data["salt"]))
        conn.commit()
        return True
    except sqlite3.IntegrityError:  # Handle duplicate usernames
        return False
    finally:
        conn.close()

def get_user(username: str) -> Optional[Dict[str, str]]:
    """
    Retrieves a user record from the database by username.
    :param username: The username to search for.
    :return: A dictionary of user data if the user exists, None otherwise.
    """
    conn: sqlite3.Connection = sqlite3.connect(DB_NAME)
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row: Optional[sqlite3.Row] = cursor.fetchone()
    conn.close()
    if row:
        return {
            "username": row[0],
            "email": row[1],
            "password_hash": row[2],
            "password_salt": row[3],
        }
    return None
