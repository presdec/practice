from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello Tkinter')
mbutton = Button(text="Hello World", state=DISABLED).grid(row=0,column=0)
mLabel = Label(text="Welcome", fg='red', bg='blue').grid(row=0,column=2)

window.mainloop()
