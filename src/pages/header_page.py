from pages.page import *


class HeaderPage(Page):
    def __init__(self, parent, name = "EmptyHeader"):
        super().__init__(parent, name)
        self.frame = Frame(self, width=150)
        self.frame.pack_propagate(False)
        self.frame.pack(side=TOP, anchor=N, fill=Y, expand=True)

        self.container = Frame(self.frame, relief=RIDGE, borderwidth=2)
        self.container.pack(side=TOP, anchor=N, fill=X)

    def add(self, name="EmptyPage", open_lambda=None):
        button = Button(self.container, text=name, command=open_lambda, font=(None, 10))
        button.pack(side=TOP, fill=X)
