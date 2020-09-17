from tkinter import Tk, Label, Button


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI")

        self.label = Label(master, text="Hello Tkinter!")
        self.label.pack()

        self.button = Button(master, text="Welcome", command=self.greet)
        self.button.pack()
        self.button2 = Button(master, text="Quit", command=master.quit)
        self.button2.pack()

    def greet(self):
        print("Welcome to Python")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
