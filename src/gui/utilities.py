from tkinter import *
from time import *


def close_and_return(root, value, command):
    root.destroy()
    if command:
        command(value)


def ask_question(title="Warning", question="Are you sure?", yes="yes", no="no", width=250, height=110, command=None):
    window = Toplevel()
    window.title(title)
    window.grab_set()
    center(window, width, height)

    frame = Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    label = Label(frame, text=question)
    label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    yes_button = Button(frame, text=yes, width=10, command=lambda: close_and_return(window, True, command))
    yes_button.grid(row=1, column=0, padx=(0, 5))

    no_button = Button(frame, text=no, width=10, command=lambda: close_and_return(window, False, command))
    no_button.grid(row=1, column=1, padx=(5, 0))


def center(root, width=1000, height=600):
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2) - 100
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
