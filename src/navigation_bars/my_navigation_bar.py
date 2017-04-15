from navigation_bars.navigation_bar import *
from pages.header_page import *


class MyNavigationBar(NavigationBar):
    def __init__(self, parent):
        super().__init__(parent)

        header = HeaderPage(self.rightFrame)
        first = Page(self.rightFrame, "First")
        second = Page(self.rightFrame, "Second")
        third = Page(self.rightFrame, "Third")

        header.add(first.name, lambda:self.open(first))
        header.add(second.name, lambda:self.open(second))
        header.add(third.name, lambda:self.open(third))

        self.add_page(header)
        self.add_page(first)
        self.add_page(second)
        self.add_page(third)