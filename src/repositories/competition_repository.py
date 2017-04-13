from domain.competition import *


class CompetitionRepository:
    def __init__(self, cnx):
        self.cnx = cnx

    def get(self, competition):
        cursor = self.cnx.cursor()
        query = "select * from COMPETITION"

        fields = []
        if competition.competitionId:
            fields.append("COMPETITION_ID=" + str(competition.competitionId))
        if competition.name:
            fields.append("NAME=\"" + str(competition.name) + "\"")
        if competition.resultType:
            fields.append("RESULT_TYPE=\"" + str(competition.resultType) + "\"")

        if len(fields) > 0:
            query += " where "
        query += " and ".join(fields) + ";"
        print(query)
        cursor.execute(query)
        result = []
        for (competitionId, name, resultType) in cursor:
            result.append(Competition(competitionId, name, resultType))
        return result

    def add(self, competition):
        cursor = self.cnx.cursor()
        query = "insert into COMPETITION ("
        fields = []
        values = []
        if competition.competitionId:
            fields.append("COMPETITION_ID")
            values.append(str(competition.competitionId))
        if competition.name:
            fields.append("NAME")
            values.append("\"" + str(competition.name) + "\"")
        if competition.resultType:
            fields.append("RESULT_TYPE")
            values.append("\"" + str(competition.resultType) + "\"")

        query += ", ".join(fields)
        query += ") values ("
        query += ", ".join(values)
        query += ");"

        print(query)

        cursor.execute(query)

    def update(self, competition):
        cursor = self.cnx.cursor()
        query = "update COMPETITION set "

        fields = []

        if competition.name:
            fields.append("NAME=\"" + str(competition.name) + "\"")
        if competition.resultType:
            fields.append("RESULT_TYPE=\"" + str(competition.resultType) + "\"")

        query += ", ".join(fields)

        query += " where COMPETITION_ID=" + str(competition.competitionId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, competition):
        cursor = self.cnx.cursor()
        query = "delete from COMPETITION where COMPETITION_ID=" + str(competition.competitionId)
        print(query)
        cursor.execute(query)