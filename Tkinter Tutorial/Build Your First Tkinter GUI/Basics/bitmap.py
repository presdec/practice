from tkinter import *


window = Tk()

window.geometry('500x500+300+150')
window.title('Hello Tkinter')
mbutton = Button(text="Hello World", bitmap='error').pack()
mbutton = Button(text="Hello World", bitmap='hourglass').pack()
mbutton = Button(text="Hello World", bitmap='info').pack()
mbutton = Button(text="Hello World", bitmap='gray75').pack()
mbutton = Button(text="Hello World", bitmap='gray50').pack()
mbutton = Button(text="Hello World", bitmap='gray25').pack()
mbutton = Button(text="Hello World", bitmap='gray12').pack()
mbutton = Button(text="Hello World", bitmap='questhead').pack()
mbutton = Button(text="Hello World", bitmap='warning').pack()
mbutton = Button(text="Hello World", bitmap='question').pack()


window.mainloop()
