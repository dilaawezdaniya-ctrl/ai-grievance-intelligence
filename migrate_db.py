import sqlite3
from pathlib import Path


db_path = Path("instance") / "grievances.db"

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(complaints)")
columns = [row[1] for row in cursor.fetchall()]

if "embedding" not in columns:
    cursor.execute(
        "ALTER TABLE complaints ADD COLUMN embedding TEXT"
    )
    connection.commit()
    print("Added embedding column.")
else:
    print("Embedding column already exists.")

connection.close()