import sqlite3
import webbrowser
x=str(input("Podaj liczbę : "))
def openbrowser():
    db = sqlite3.connect('run_webbrowser2_0.db')
    cursor = db.cursor()

    query = f'SELECT Link FROM score where id =={x}'
    cursor.execute(query)
    rows= cursor.fetchall()
    # webbrowser.open(str(rows).replace('[','').replace(']',''))
    print(rows[0])
    # db.commit()
    # db.close()



openbrowser()