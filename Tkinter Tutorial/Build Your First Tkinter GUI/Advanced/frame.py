from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('450x300')

frame = ttk.Frame(root)
frame.pack()

frame.config(height=200, width=400)
frame.config(relief = RIDGE, padding=(50, 25))

ttk.Button(frame, text="frame").pack()

L = ttk.LabelFrame(root, height = 200, width=400, text='My Frame', padding=(50, 50))
L.pack()

ttk.Button(L, text="frame").pack()

root.mainloop()
