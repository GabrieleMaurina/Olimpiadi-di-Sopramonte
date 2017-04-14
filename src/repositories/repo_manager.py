from mysql.connector import *

from domain.athlete import *
from domain.athlete_competition import *
from domain.category import *
from domain.competition import *
from domain.result import *
from domain.team import *
from repositories.athlete_repository import *
from repositories.athlete_competition_repository import *
from repositories.category_repository import *
from repositories.competition_repository import *
from repositories.result_repository import *
from repositories.team_repository import *

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

        self.athleteRepository = AthleteRepository(self.cnx)
        self.athleteCompetitionRepository = AthleteCompetitionRepository(self.cnx)
        self.categoryRepository = CategoryRepository(self.cnx)
        self.competitionRepository = CompetitionRepository(self.cnx)
        self.resultRepository = ResultRepository(self.cnx)
        self.teamRepository = TeamRepository(self.cnx)

    def __del__(self):
        self.cnx.close()