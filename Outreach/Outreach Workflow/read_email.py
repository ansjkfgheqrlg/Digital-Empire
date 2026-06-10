import sqlite3
conn = sqlite3.connect("output/leads.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tabelle:", [r[0] for r in cur.fetchall()])
cur.execute("SELECT COUNT(*) FROM leads_contattati")
print("Totale lead nel DB:", cur.fetchone()[0])
cur.execute("SELECT page_name, email, oggetto, corpo, stato FROM leads_contattati WHERE oggetto IS NOT NULL AND oggetto != '' LIMIT 1")
row = cur.fetchone()
if row:
    print("---")
    print("Business:", row["page_name"])
    print("Email:", row["email"])
    print("Stato:", row["stato"])
    print("OGGETTO:", row["oggetto"])
    print("\nCORPO:")
    print(row["corpo"])
else:
    print("Nessuna email trovata con oggetto")
conn.close()
