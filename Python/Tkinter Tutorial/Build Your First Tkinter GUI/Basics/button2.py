from tkinter import *


window = Tk()

window.geometry('500x500')
window.title('Hello Tkinter')
photo = PhotoImage(file='./1.png')
mbutton = Button(text="Hello Tkinter", width=138, height=138, bg='green', fg='white',
                 activebackground='red', activeforeground='blue', bd=5,
                 cursor='hand1', state=NORMAL, image=photo, highlightthickness=5).pack()


window.mainloop()
