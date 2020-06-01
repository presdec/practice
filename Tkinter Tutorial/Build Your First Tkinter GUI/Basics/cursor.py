from tkinter import *


window = Tk()

window.geometry('500x500+300+150')
window.title('Hello Tkinter')
mbutton = Button(text="Hello World", relief=RAISED, cursor='circle').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='heart').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='plus').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='clock').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='dotbox').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='man').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='mouse').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='pirate').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='sizing').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='star').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='hand2').pack()
mbutton = Button(text="Hello World", relief=RAISED, cursor='boat').pack()


window.mainloop()
