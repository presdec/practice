from tkinter import *


master = Tk()
master.geometry('200x70')


def Show_Entry():
    print('Name:%s\npassword:%s'%(e1.get(), e2.get()))

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label(master,text='Name').grid(row=0)
Label(master,text='Password').grid(row=1)

Button(master,text='Quit', command=master.quit).grid(row=2,column=0)
Button(master,text='Show', command=Show_Entry).grid(row=2,column=1)

mainloop()
