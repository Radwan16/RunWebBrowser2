import tkinter as t
import webbrowser
import sqlite3
from show_records import show_records
from add_records import add_records
db = sqlite3.connect('run_webbrowser2_0.db')
cursor= db.cursor()

window = t.Tk()
window.title('Run web')
window.geometry("250x150")
show_records()
entry = t.Entry(window, width=10, justify='center')
entry.pack()

def open():
    query = f"SELECT Link FROM score WHERE id == ?"
    link_id = entry.get()
    cursor.execute(query,(link_id))
    link = cursor.fetchone()

    if link is None:
        t.messagebox.showinfo("Błąd", "Nie znaleziono linku o podanym identyfikatorze")
    else:
        webbrowser.open(link[0])


button = t.Button(window, text="OK", command=open).pack()
button2 = t.Button(window, text="+",command=add_records)
button2.place(relx=1,rely=0, anchor="ne")

window.mainloop()
db.close()