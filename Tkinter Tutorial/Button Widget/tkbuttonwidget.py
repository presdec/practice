from tkinter import*
from tkinter import messagebox


top = Tk()
top.geometry("240x150")


def hellocallback():
    msg = messagebox.showinfo("click me", "Hello Tkinter Button")


b = Button(top,text="Click me for TK inter", command=hellocallback)
b.place(x=50, y=50)
top.mainloop()
