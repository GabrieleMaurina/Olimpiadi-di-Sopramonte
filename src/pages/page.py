from tkinter import *

class Page(Frame):
    def __init__(self, parent, name="EmptyPage"):
        super().__init__(parent)
        self.name = name
        l = Label(self, text=self.name)
        l.pack()