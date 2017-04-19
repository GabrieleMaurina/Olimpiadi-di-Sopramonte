from tkinter import *

from navigation_bars.my_navigation_bar import *


class Olympics:

    title = "Olimpiadi Di Sopramonte 2017"

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title(Olympics.title)

        self.frame = Frame(self.root, relief=RIDGE, borderwidth=2)
        self.frame.pack(side=TOP, anchor=N, fill=X, padx=(10, 10), pady=(10, 10))

        self.title = Label(self.frame, text=Olympics.title, font=(None, 20))
        self.title.pack(side=TOP, pady=(10, 10))

        self.navigationBar = MyNavigationBar(self.root)

        self.root.mainloop()
