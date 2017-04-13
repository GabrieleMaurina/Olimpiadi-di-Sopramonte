from mysql.connector import *

from domain.athlete import *
from domain.athlete_competition import *
from domain.category import *
from repositories.athlete_repository import *
from repositories.athlete_competition_repository import *
from repositories.category_repository import *

class RepoManager:

    user = "sql11166605"
    password = "FctpTVkSmB"
    database = "sql11166605"
    host = "sql11.freemysqlhosting.net"
    port = "3306"

    def __init__(self):
        self.repo = {}

        self.cnx = connect(user=RepoManager.user, password=RepoManager.password, database=RepoManager.database, host=RepoManager.host, port=RepoManager.port)
        self.cnx.autocommit = True

        self.add(Athlete, AthleteRepository(self.cnx))
        self.add(AthleteCompetition, AthleteCompetitionRepository(self.cnx))
        self.add(Category, CategoryRepository(self.cnx))

    def __del__(self):
        self.cnx.commit()
        self.cnx.close()

    def get(self, table):
        return self.repo[table]

    def add(self, table, repo):
        self.repo[table] = repo

    def remove(self, table):
        del self.repo[table]