from repositories.repo_manager import *

repo = RepoManager()

for competition in repo.competitionRepository.get(Competition()):
    print(competition)