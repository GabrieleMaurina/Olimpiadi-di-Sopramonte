from repositories.repo_manager import *
from navigation_bars.my_navigation_bar import *

#from tkinter import *
from domain.result import *

#root = Tk()
#root.geometry("500x500")

#bar = MyNavigationBar(root)

#root.mainloop()
print("asdf")
repoManager = RepoManager()
#repoManager.teamRepository.add(Team(name="le incredibili marmotte",color="00cc00",comp_num_min=2,comp_num_max=50,race_time_male=0.02,race_time_female=0.01))
r = repoManager.teamRepository.get(Team(comp_num_min=2))
for(Result) in r:
    print(Result.__str__())