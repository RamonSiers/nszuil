from tkinter import *
from functools import partial

def onclick(message):
    label["text"] = message

root = Tk()
label = Label(master=root, text='Is papa dik', height=2)
label.pack()

buttonA = Button(master=root, text='Ja', command=partial(onclick, "Juist"))
buttonA.pack()

buttonB = Button(master=root, text='Nee', command=partial(onclick, "Onjuist"))
buttonB.pack(pady=10)

root.mainloop()