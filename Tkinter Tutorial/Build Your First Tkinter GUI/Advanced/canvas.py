from tkinter import *

root = Tk()
root.geometry('300x300')

canvas = Canvas(root, width=300, height=250, bg='green')
canvas.pack()

# [START X], [START Y], [LENGTHX], [LENGTHY]
r = canvas.create_rectangle(30, 20, 200, 100, fill='blue')

ball = canvas.create_oval(10, 10, 60, 60, fill='red')
root.mainloop()
