from tkinter import *


window = Tk()

window.geometry('500x500')
window.title('Hello Tkinter')


def hello():
    L = Label(text='enter', fg='#c860c9', bg='orange', font=10).pack()


def delete():
    L2 = Label(text='delete', fg='orange', bg='yellow', font=10).pack()


MyLabel = Label(text='Welcome', fg='#646060', bg='#F87217', font=10).pack()
MyButton = Button(text='Enter', fg='gray', bg='plum', command=hello, font=20).pack()
MyButton = Button(text='Deleted', fg='gray', bg='plum', command=delete, font=20).pack()

window.mainloop()
