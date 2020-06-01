from tkinter import *


old = Tk()
new = Tk()


def hello():
    m = b.get()
    L = Label(text=m, fg='#c860c9', bg='orange', font=10).pack()


def delete():
    L2 = Label(new, text='delete', fg='orange', bg='yellow', font=10).pack()


old.geometry('500x500+100+200')
new.geometry('500x500+700+200')

old.title('Hello Tkinter')
new.title('Tkinter')


b = StringVar()
MyLabel = Label(text='Welcome', fg='#646060', bg='#F87217', font=10).pack()
MyButton1 = Button(text='Enter', fg='gray', bg='plum', command=hello, font=20).pack()
MyButton2 = Button(new, text='quit', fg='gray', bg='plum', command=old.quit, font=20).pack()
MyButton3 = Button(new, text='delete', fg='gray', bg='plum', command=delete, font=20).pack()

text = Entry(textvariable=b).pack()

old.mainloop()
