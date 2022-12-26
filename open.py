import sqlite3
db= sqlite3.connect('run_webbrowser2_0.db')
cursor = db.cursor()

query = "SELECT Link FROM score WHERE id = 2 "
cursor.execute(query)
rows = cursor.fetchone()

for r in rows:
    print(r)

db.commit()
db.close()
