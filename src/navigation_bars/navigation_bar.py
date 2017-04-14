from tkinter import *

class NavigationBar(Frame):

    def __init__(self, parent):
        super().__init__(parent, bg = 'black')

        self.pack(fill=BOTH, expand=True)

        self.leftFrame = Frame(self, width = 100, bg = 'pink')
        self.rightFrame = Frame(self, bg = 'yellow')

        self.leftFrame.pack(side=LEFT, fill=Y)
        self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.pages = []
        self.buttons = []
        self.current = -1

    def add_page(self, page):
        self.pages.append(page)
        name = page.__class__.__name__
        if hasattr(page, "name"):
            name = page.name
        button = Button(self.leftFrame, text=name, height = 1, width = 10, command=lambda : self.open(page))
        self.buttons.append(button)
        button.pack(fill=X)
        if len(self.pages) == 1:
            self.open(page)
        return page

    def open(self, page):
        index = self.pages.index(page)
        self.current = index
        self.update_ui()

    def update_ui(self):
        for index, page in enumerate(self.pages):
            if index == self.current:
                page.pack(side=TOP, fill=BOTH, expand=True)
            else:
                page.pack_forget()
        for index, button in enumerate(self.buttons):
            if index == self.current:
                button.configure(bg='green')
            else:
                button.configure(bg='white')