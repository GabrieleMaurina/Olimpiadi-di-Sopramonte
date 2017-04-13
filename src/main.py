from repositories.repo_manager import *

repo = RepoManager()

'''repo.get(Athlete).add(Athlete(name = "Allison", surname="Tyler"))
print(repo.get(Athlete).get(Athlete(id = 34)))
repo.get(Athlete).remove(Athlete(athlete_id=35))
repo.get(Athlete).update(Athlete(athlete_id = 34, name="Hugo"))
for athlete in repo.get(Athlete).get(Athlete(name="Allison")):
    print(athlete)'''

'''repo.get(Category).add(Category(name="froci", min_age=52))
repo.get(Category).update(Category(category_id=5, min_age=11))
repo.get(Category).remove(Category(category_id=5))
for category in repo.get(Category).get(Category(name="froci")):
    print(category)'''