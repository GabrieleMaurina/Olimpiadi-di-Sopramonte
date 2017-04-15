from navigation_bars.my_navigation_bar import *
from tkinter import *


class OlimpiadiDiSopramonte:
    def __init__(self):
        root = Tk()
        root.geometry("500x500")

        title = Label(root, text="Olimpiadi Di Sopramonte", font=(None, 20))

        title.pack(side=TOP)

        MyNavigationBar(root)
        root.mainloop()