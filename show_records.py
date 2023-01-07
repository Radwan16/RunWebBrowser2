import sqlite3
import tkinter as t

def show_records():
    window = t.Tk()
    db = sqlite3.connect('run_webbrowser2_0.db')
    cursor = db.cursor()
    query = 'SELECT id, Nazwa FROM score;'
    cursor.execute(query)
    rows= cursor.fetchall()
    for r in rows:
        r = t.Label(text=r).pack()
    db.commit()
    db.close()
    window.destroy()


