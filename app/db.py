import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "focus_monitor.db"


def insert_log(timestamp, app_name, window_title, status, idle_seconds=0):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO activity_logs (
            timestamp,
            app_name,
            window_title,
            status,
            idle_seconds
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        timestamp,
        app_name,
        window_title,
        status,
        idle_seconds
    ))

    conn.commit()
    conn.close()


def get_recent_logs(limit=100):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM activity_logs
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows