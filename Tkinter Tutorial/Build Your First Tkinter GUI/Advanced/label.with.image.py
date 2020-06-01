from tkinter import *
from tkinter import ttk

window = Tk()


label = ttk.Label(window, text="Hello Tkinter")
label.pack()
label.config(foreground='silver', background='brown')
label.config(font=('Fiera', 20, 'bold'))

label.config(wraplength=100)
label.config(justify=CENTER)

logo = PhotoImage(file='1.png')
label.config(image=logo)
label.config(compound='left')

window.wm_attributes('-alpha', 0.7)
window.mainloop()
