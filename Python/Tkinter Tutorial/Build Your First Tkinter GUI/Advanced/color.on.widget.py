from tkinter import *

root = Tk()
#root.geometry('500x500')

frame_Toolbar = Frame(root, bg='Red', height=80)
frame_botom = Frame(root, bg='green', height=20)
frame_Middle = Frame(root, bg='blue', height=250)


frame_Toolbar.pack(fill='x', side=TOP)
frame_botom.pack(fill='x', side=BOTTOM)
frame_Middle.pack(fill='x', side=TOP, expand=YES)

root.mainloop()
