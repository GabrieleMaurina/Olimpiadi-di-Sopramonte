from tkinter import *
import tkinter.ttk as ttk
from repositories.repo_manager import *
from navigation_bars.my_navigation_bar import *
from gui.utilities import *


class Olympics:

    title = "Olimpiadi Di Sopramonte 2017"

    def __init__(self):

        self.width = 900
        self.height = 600

        self.root = Tk()
        self.root.title(Olympics.title)

        self.frame = Frame(self.root, relief=RIDGE, borderwidth=2)
        self.frame.pack(side=TOP, anchor=N, fill=X, padx=(10, 10), pady=(10, 10))

        self.title = Label(self.frame, text=Olympics.title, font=(None, 20))
        self.title.pack(side=TOP, pady=(10, 10))

        self.repoManager = RepoManager()

        self.navigationBar = MyNavigationBar(self.root, self.repoManager)

        center(self.root, self.width, self.height)

        self.root.mainloop()
