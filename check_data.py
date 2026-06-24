import sqlite3

conn = sqlite3.connect("focus_monitor.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM activity_logs")
print("Rows:", cursor.fetchone()[0])

cursor.execute("SELECT * FROM activity_logs LIMIT 5")
print(cursor.fetchall())

conn.close()