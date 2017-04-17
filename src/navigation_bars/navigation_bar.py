from pages.header_page import *
from tkinter import *

class NavigationBar(Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill=BOTH, expand=True)

        self.leftFrame = Frame(self, width = 150, relief=RIDGE, borderwidth=2)
        self.rightFrame = Frame(self, relief=RIDGE, borderwidth=2)

        self.leftFrame.pack_propagate(False)

        self.leftFrame.pack(side=LEFT, anchor=NW, fill=Y, padx=(10, 5), pady=(0, 10))
        self.rightFrame.pack(side=RIGHT,anchor=NE, fill=BOTH, expand=True, padx=(5, 10), pady=(0, 10))

        self.pages = []
        self.buttons = []
        self.current = -1

        self.bind_all("<MouseWheel>", self.handle_mouse_wheel)
        for i in range(10):
            self.bind_all(str(i), self.handle_numbers)

    def handle_numbers(self, event):
        number = int(event.char)
        number -= 1
        if number < 0:
            number = 9
        if number < len(self.pages):
            self.current = number
            self.update_ui()

    def handle_mouse_wheel(self, event):
        if event.delta > 0:
            self.current += 1
            self.current %= len(self.pages)
            self.update_ui()
        if event.delta < 0:
            self.current -= 1
            if self.current < 0:
                self.current += len(self.pages)
            self.update_ui()

    def add_page(self, page):
        self.pages.append(page)
        name = page.__class__.__name__
        if hasattr(page, "name"):
            name = page.name

        font = (None, 10)
        padx = (20, 0)
        if issubclass(type(page), HeaderPage):
            font = (None, 12, "bold")
            padx = (0, 0)
        button = Button(self.leftFrame, text=name, command=lambda:self.open(page), font=font)
        self.buttons.append(button)
        button.pack(side=TOP, fill=X, padx=padx)
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
                button.configure(bg="gray")
            else:
                button.configure(bg="SystemButtonFace")
