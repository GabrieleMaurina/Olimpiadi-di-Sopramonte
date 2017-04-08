from repositories.repo_manager import *

repo = RepoManager()

repo.get(Athlete).add(Athlete(name = "Mark", surname="Cuban"))

print(repo.get(Athlete).get(Athlete(id = 35)))


for athlete in repo.get(Athlete).getAll():
    print(athlete)