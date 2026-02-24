import sqlite3

def init_db():
    conn = sqlite3.connect("doctors.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_doctor(name: str, score: int):
    conn = sqlite3.connect("doctors.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO doctors (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

def get_doctor_history(name: str):
    conn = sqlite3.connect("doctors.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT score, created_at FROM doctors WHERE LOWER(name) = LOWER(?) ORDER BY created_at DESC LIMIT 5",
        (name,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_doctors():
    conn = sqlite3.connect("doctors.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, score, created_at 
        FROM doctors 
        ORDER BY created_at DESC 
        LIMIT 20
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows
