import tkinter as tk

master = tk.Tk()
master.geometry('400x400')


S1 = tk.Scale(master, from_=0, to=100)
S1.set(45)
S1.grid(row=0, column=0)

S2 = tk.Scale(master, from_=30, to=3000, resolution=100)
S2.set(15)
S2.grid(row=0, column=1)

master.mainloop()
