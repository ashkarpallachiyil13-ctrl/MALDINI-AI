import sqlite3

# ==========================
# Configuration
# ==========================

DATABASE_NAME = "maldini.db"

# ==========================
# Database Connection
# ==========================

def get_connection():
    """
    Returns a connection to the SQLite database.
    """

    return sqlite3.connect(DATABASE_NAME)


# ==========================
# Database Initialization
# ==========================

def initialize_database():
    """
    Creates the required tables if they do not exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Conversation list
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Messages inside each conversation
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (conversation_id)
            REFERENCES conversations(id)
            ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


# ==========================
# Run Directly
# ==========================

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")