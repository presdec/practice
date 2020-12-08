import sys
from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter import Tk

def vp_start_gui():
    global window
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
    window.update()
    window.configure(bg=c)

    label = ttk.Label(window, text=c + '\ncopied')
    label.config(foreground='black', background=c,font=('Fiera', 60, 'bold'))
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    ttk.Button(window, text="quit", compound=CENTER, command=window.quit).grid(row=1)

    window.mainloop()


if __name__ == '__main__':
    def refresh():
        window.destroy()
        vp_start_gui()

    vp_start_gui()
