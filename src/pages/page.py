from tkinter import *

class Page(Frame):
    def __init__(self, parent, name="EmptyPage"):
        super().__init__(parent)
        self.name = name
        self.label = Label(self, text=self.name, font=(None, 15))
        self.label.pack(pady = (10, 10))
