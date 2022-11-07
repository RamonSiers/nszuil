from tkinter import *
import psycopg2

connection_string = "host='localhost' dbname='Databese Zuil' user='postgres' password='kaas'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
query = """SELECT  tekst_bericht, naam_reiziger
        FROM bericht
        WHERE status_beoordeling = 'g' ;"""
cursor.execute(query)
records = cursor.fetchall()             # retrieve the records from the database
conn.close()
tekstblok = ''
for record in records:
    tekstblok = tekstblok + record[0] + ': ' + record[1] + '\n'



root = Tk()

import tkinter as tk

root = tk.Tk()
img = tk.PhotoImage(file="'WeeDenseArabianwildcat-size_restricted.gif")
lab = tk.Label(root, text=f"{tekstblok}")
lab.grid()
lab["compound"] = tk.LEFT
lab["image"] = img

root.mainloop()

root.mainloop()

