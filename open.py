import sqlite3
import webbrowser

db = sqlite3.connect('run_webbrowser2_0.db')
cursor = db.cursor()
x=str(input("Podaj liczbę : "))
def openbrowser():

    query = f'SELECT Link FROM score where id =={x}'
    cursor.execute(query)
    rows= cursor.fetchall()
    for r in rows:
        webbrowser.open(str(r[0]))
    # db.commit()
    # db.close()



openbrowser()