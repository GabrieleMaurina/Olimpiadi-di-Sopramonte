from repositories.repo_manager import *

repo = RepoManager()

#repo.get(Athlete).add(Athlete(name = "Mark", surname="Cuban"))

#print(repo.get(Athlete).get(Athlete(id = 35)))

#repo.get(Athlete).remove(Athlete(athlete_id=35))

repo.get(Athlete).update(Athlete(athlete_id = 34, gender="Male"))

for athlete in repo.get(Athlete).getAll():
    print(athlete)