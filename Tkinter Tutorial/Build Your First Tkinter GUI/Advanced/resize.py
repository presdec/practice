from tkinter import *
from tkinter import ttk


def resize(ev=None):
    label.configure(font='Arial -%d bold' % scale.get())


window = Tk()
window.geometry('500x500')

label = ttk.Label(window, text='Hello Tkinter')
label.pack(expand=1, fill = 'y')
label.config(foreground='silver', background='brown')

scale = ttk.Scale(window, from_=10, to=60, command=resize)
scale.pack()

quit = ttk.Button(window, text='Quit', command=window.quit)
quit.pack()


window.mainloop()
