from tkinter import *
from tkinter import ttk
'''In Tkinter, a callback is Python code that is called by Tk when something
 happens. For example, the Button widget provides a command callback which is
 called when the user clicks the button. You also use callbacks with event
 bindings.'''

window = Tk()


def callback(number):
    print(number)


ttk.Button(window, text="Click Me", command=lambda: callback(1)).pack()
ttk.Button(window, text="Click Me", command=lambda: callback(2)).pack()
ttk.Button(window, text="Click Me", command=lambda: callback(3)).pack()
ttk.Button(window, text="Click Me", command=lambda: callback(4)).pack()
ttk.Button(window, text="Click Me", command=lambda: callback(5)).pack()

window.mainloop()
