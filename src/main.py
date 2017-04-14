from repositories.repo_manager import *
from navigation_bars.my_navigation_bar import *

from tkinter import *

root = Tk()
root.geometry("500x500")

bar = MyNavigationBar(root)

root.mainloop()
