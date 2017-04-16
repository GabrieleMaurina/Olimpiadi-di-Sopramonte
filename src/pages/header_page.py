from pages.page import *


class HeaderPage(Page):
    def __init__(self, parent, name = "EmptyHeader"):
        super().__init__(parent, name)

    def add(self, name="EmptyPage", open_lambda=None):
        button = Button(self, text=name, height = 1, width = 10, command=open_lambda, font=(None, 10))
        button.pack(side=TOP)