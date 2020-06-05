from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry('+200+200')

button = ttk.Button(window, text="Click Me")
button.pack()


def callback():
    print('Photo')


logo = PhotoImage(file = './1.png')

button.config(command = callback, image=logo, compound = LEFT)

window.mainloop()
