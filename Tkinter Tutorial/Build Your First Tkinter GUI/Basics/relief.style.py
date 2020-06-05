from tkinter import *


window = Tk()

window.geometry('500x500+300+150')
window.title('Hello Tkinter')
mbutton = Button(text="Hello World", relief=SUNKEN).pack()
mbutton = Button(text="Hello World", relief=FLAT).pack()
mbutton = Button(text="Hello World", relief=GROOVE).pack()
mbutton = Button(text="Hello World", relief=RAISED).pack()
mbutton = Button(text="Hello World", relief=RIDGE).pack()


window.mainloop()
