from navigation_bars.navigation_bar import *
from pages.page import *


class MyNavigationBar(NavigationBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_page(Page(self.rightFrame, "First"))
        self.add_page(Page(self.rightFrame, "Second"))
        self.add_page(Page(self.rightFrame, "Third"))