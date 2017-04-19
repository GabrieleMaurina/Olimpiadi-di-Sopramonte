from tkinter import *
from repositories.repo_manager import *
from navigation_bars.my_navigation_bar import *


class Olympics:

    title = "Olimpiadi Di Sopramonte 2017"

    def __init__(self):

        self.width = 1000
        self.height = 600

        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.title(Olympics.title)

        self.frame = Frame(self.root, relief=RIDGE, borderwidth=2)
        self.frame.pack(side=TOP, anchor=N, fill=X, padx=(10, 10), pady=(10, 10))

        self.title = Label(self.frame, text=Olympics.title, font=(None, 20))
        self.title.pack(side=TOP, pady=(10, 10))

        self.repoManager = RepoManager()

        self.navigationBar = MyNavigationBar(self.root, self.repoManager)

        self.center()

        self.root.mainloop()

    def center(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.height // 2) - 100
        self.root.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))
