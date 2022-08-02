import sqlite3
# import pyttsx3
import webbrowser
import tkinter as t
from show_records import show_records

# engine = pyttsx3.init()
window= t.Tk()
window.title("RunWebBrowser 2.0")
window.geometry("500x300")

show_records()

db = sqlite3.connect('run_webbrowser2_0.db')
cursor = db.cursor()

entry = t.Entry(window, width=10,justify='center').pack()
def open():
    global entry
    query = f'SELECT * FROM score WHERE id=={entry}'

    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        webbrowser.open(str(r[2]))

t.Button(window,text="OK", command=open).pack()

window.mainloop()

db.commit()
db.close()
