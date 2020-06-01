from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter import Tk

window = Tk()

window.geometry('500x500')
window.title('Hello Tkinter')

c = []
b = StringVar()
b = colorchooser.askcolor(initialcolor='#FFFFFF')
word_list = list(b)  # list of words
c = word_list[-1]

window.clipboard_clear()
window.clipboard_append(c)
window.update() # now it stays on the clipboard after the window is closed


window.configure(bg=c)

label = ttk.Label(window, text=c + '\ncopied')
label.config(foreground='silver', background=c)
label.config(font=('Fiera', 60, 'bold'))
label.place(relx=0.5, rely=0.5, anchor=CENTER)
# label.config(wraplength=100)
label.config(justify=CENTER, )

ttk.Button(window, text="quit", compound=CENTER, command=window.quit).grid(row=1)
ttk.Button(window, text="again", compound=CENTER, command=window.quit).grid(row=2)

window.mainloop()
