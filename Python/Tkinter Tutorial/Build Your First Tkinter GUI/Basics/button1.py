from tkinter import *


window = Tk()

window.geometry('500x500+300+150')
window.title('Hello Tkinter')
mbutton = Button(text="Hello World", width=30, height=25, bg='green', fg='white',
                 activebackground='red', activeforeground='blue', bd=30,
                 cursor='hand1').pack()\


window.mainloop()
