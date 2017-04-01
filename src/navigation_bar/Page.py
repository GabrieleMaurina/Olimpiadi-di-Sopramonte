from tkinter import *

class Page(Frame):
    name = "Empty Page"
    def __init__(self, parent):
        super().__init__(parent)
        l = Label(self, text="HELLO")
        l.pack()