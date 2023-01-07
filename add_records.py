import tkinter as t
import sqlite3
def add_records():
    window2 = t.Tk()
    window2.title("Add records")
    window2.geometry("250x150")
    t.Label(window2, text="Nazwa").pack()
    entry1 = t.Entry (window2, width=10)
    entry1.pack()
    t.Label(window2, text="Link").pack()
    entry2 = t.Entry(window2, width=10)
    entry2.pack()

    def add_records2():
        nazwa = entry1.get()
        link  = entry2.get()
        db = sqlite3.connect('run_webbrowser2_0.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO score (nazwa,link) VALUES(? , ?)",(nazwa, link))

        db.commit()
        db.close()
        entry1.delete(0,"end")
        entry2.delete(0,"end")
        window2.destroy()
    t.Button(window2, text="Dodaj",command=add_records2).pack()
    window2.mainloop()


