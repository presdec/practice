from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
    statusbar.config(text="View Updated")
    statusbar.update_idletasks()


def search_command():
    list1.delete(0, END)
    for row in backend.search(titletext.get(), authortext.get(), yeartext.get(), isbntext.get()):
        list1.insert(END, row)
    statusbar.config(text="Search Results")
    statusbar.update_idletasks()


def add_command():
    backend.insert(titletext.get(), authortext.get(), yeartext.get(), isbntext.get())
    list1.delete(0, END)
    list1.insert(END, (titletext.get(), authortext.get(), yeartext.get(), isbntext.get()))
    statusbar.config(text="Book Added")
    statusbar.update_idletasks()


def delete_command():
    backend.delete(selected_tuple[0])
    statusbar.config(text="Book Deleted")
    statusbar.update_idletasks()


def update_command():
    backend.update(selected_tuple[0], titletext.get(), authortext.get(), yeartext.get(), isbntext.get())
    view_command()
    statusbar.config(text=("Updated", selected_tuple[0], titletext.get(), authortext.get(), yeartext.get(), isbntext.get()))
    statusbar.update_idletasks()


window = Tk()
window.resizable(0,0)
window.title("Book Catalogue")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

titletext = StringVar()
e1 = Entry(window, textvariable=titletext)
e1.grid(row=0, column=1)

authortext = StringVar()
e2 = Entry(window, textvariable=authortext)
e2.grid(row=0, column=3)

yeartext = StringVar()
e3 = Entry(window, textvariable=yeartext)
e3.grid(row=1, column=1)

isbntext = StringVar()
e4 = Entry(window, textvariable=isbntext)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, sticky="nsew")

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky="ns")

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)


statusbar = Label(window,text="", bd=1, relief=SUNKEN, anchor=W)
statusbar.grid(row=9,  columnspan=6, sticky="ew")

window.mainloop()