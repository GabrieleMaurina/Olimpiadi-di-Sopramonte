from domain.athlete_competition import *


class AthleteCompetitionRepository:
    def __init__(self, cnx):
        self.cnx = cnx

    def get(self, athlete_competition):
        cursor = self.cnx.cursor()
        query = "select * from ATHLETE_COMPETITION"

        fields = []
        if athlete_competition.athleteId:
            fields.append("ATHLETE_ID=" + str(athlete_competition.athleteId))
        if athlete_competition.competitionId:
            fields.append("COMPETITION_ID=" + str(athlete_competition.competitionId))
        if athlete_competition.placement:
            fields.append("PLACEMENT=" + str(athlete_competition.placement))
        if athlete_competition.score:
            fields.append("SCORE=" + str(athlete_competition.score))

        if len(fields) > 0:
            query += " where "
        query += " and ".join(fields) + ";"
        print(query)
        cursor.execute(query)

        result = []
        for (athleteId, competitionId, placement, score) in cursor:
            result.append(AthleteCompetition(athleteId, competitionId, placement, score))
        return result

    def add(self, athlete_competition):
        cursor = self.cnx.cursor()
        query = "insert into ATHLETE_COMPETITION ("
        fields = []
        values = []
        if athlete_competition.athleteId:
            fields.append("ATHLETE_ID")
            values.append(str(athlete_competition.athleteId))
        if athlete_competition.competitionId:
            fields.append("COMPETITION_ID")
            values.append(str(athlete_competition.competitionId))
        if athlete_competition.placement:
            fields.append("PLACEMENT")
            values.append(str(athlete_competition.placement))
        if athlete_competition.score:
            fields.append("SCORE")
            values.append(str(athlete_competition.score))

        query += ", ".join(fields)
        query += ") values ("
        query += ", ".join(values)
        query += ");"

        print(query)

        cursor.execute(query)

    def update(self, athlete_competition):
        cursor = self.cnx.cursor()
        query = "update ATHLETE_COMPETITION set "

        fields = []

        if athlete_competition.placement:
            fields.append("PLACEMENT=\"" + str(athlete_competition.placement) + "\"")
        if athlete_competition.score:
            fields.append("SCORE=\"" + str(athlete_competition.score) + "\"")

        query += ", ".join(fields)

        query += " where ATHLETE_ID=" + str(athlete_competition.athleteId) + " and COMPETITION_ID=" + str(athlete_competition.competitionId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, athlete_competition):
        cursor = self.cnx.cursor()
        query = "delete from ATHLETE_COMPETITION where ATHLETE_ID=" + str(athlete_competition.athleteId) + " and COMPETITION_ID=" + str(athlete_competition.competitionId) + ";"
        print(query)
        cursor.execute(query)