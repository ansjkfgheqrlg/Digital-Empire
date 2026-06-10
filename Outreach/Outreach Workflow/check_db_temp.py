import sqlite3
import os

db_path = r'c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow\output\leads.db'
if not os.path.exists(db_path):
    print(f"File not found: {db_path}")
else:
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()
    curr.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = curr.fetchall()
    print(f"Tables: {tables}")
    for table in tables:
        t_name = table[0]
        curr.execute(f"SELECT COUNT(*) FROM {t_name}")
        count = curr.fetchone()[0]
        print(f"Table {t_name}: {count} rows")
    conn.close()
