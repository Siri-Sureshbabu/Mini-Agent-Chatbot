import sqlite3

def get_connection():
    return sqlite3.connect("chat_logs.db")

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            question TEXT,
            tool_used TEXT,
            response TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_chat(question, tool_used, response):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO chats VALUES (?, ?, ?)",
        (question, tool_used, response)
    )

    conn.commit()
    conn.close()