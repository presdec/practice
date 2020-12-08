from tkinter import *
from tkinter import ttk

root = Tk()

combo = ttk.Combobox(root)
combo.pack()

combo.config(value = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

combo.set('Feb')
print('Dec')

spin = Spinbox(root, from_=1990, to=2020).pack()
print('2000')

root.mainloop()
