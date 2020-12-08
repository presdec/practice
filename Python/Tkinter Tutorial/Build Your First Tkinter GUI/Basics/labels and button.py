from tkinter import *

window = Tk()

window.geometry('500x500+300+150')
window.title('Hello Tkinter')
mbutton = Button(text="Hello World", state=DISABLED).pack(pady=10)
mLabel = Label(text="Welcome", fg='red', bg='blue').pack()

window.mainloop()
