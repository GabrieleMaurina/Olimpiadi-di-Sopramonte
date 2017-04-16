from tkinter import *

from navigation_bars.my_navigation_bar import *


class OlimpiadiDiSopramonte:

    title = "Olimpiadi Di Sopramonte"

    def __init__(self):
        root = Tk()
        root.geometry("500x500")
        root.title(OlimpiadiDiSopramonte.title)

        title = Label(root, text=OlimpiadiDiSopramonte.title, font=(None, 20), height=2)

        title.pack(side=TOP)

        MyNavigationBar(root)
        root.mainloop()