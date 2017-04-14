from domain.result import *

class ResultRepository:
    def __init__(self,cnx):
        self.cnx = cnx

    def get(self,result):
        cursor = self.cnx.cursor()
        query = "select * from RESULT"
        fields = []
        if result.resultId:
            fields.append("RESULT_ID = " + str(result.resultId))
        if result.athleteId:
            fields.append("ATHLETE_ID = " + str(result.athleteId))
        if result.competitionId:
            fields.append("COMPETITION_ID = " + str(result.competitionId))
        if result.resultValue:
            fields.append("RESULT_VALUE = " + str(result.resultValue))
        if result.mistakes:
            fields.append("MISTAKES = " + str(result.mistakes))

        if len(fields) > 0:
            query += " where "
        query += " and ".join(fields) + ";"
        print(query)
        cursor.execute(query)
        result = []
        for (resultId,athleteId,competitionId,resultValue,mistakes) in cursor:
            result.append(Result(resultId,athleteId,competitionId,resultValue,mistakes))
        return result

    def add(self, result):
        cursor = self.cnx.cursor()
        query = "insert into RESULT ("
        fields = []
        values = []
        if result.resultId:
            fields.append("RESULT_ID")
            values.append(str(result.resultId))
        if result.athleteId:
            fields.append("ATHLETE_ID")
            values.append(str(result.athleteId))
        if result.competitionId:
            fields.append("COMPETITION_ID")
            values.append(str(result.competitionId))
        if result.resultValue:
            fields.append("RESULT_VALUE")
            values.append(str(result.resultValue))
        if result.mistakes:
            fields.append("MISTAKES")
            values.append(str(result.mistakes))

        query += ", ".join(fields)
        query += ") values ("
        query += ", ".join(values)
        query += ");"

        print(query)

        cursor.execute(query)

    def update(self, result):
        cursor = self.cnx.cursor()
        query = "update RESULT set "

        fields = []

        if result.resultValue:
            fields.append("RESULT_VALUE = " + str(result.resultValue))
        if result.mistakes:
            fields.append("MISTAKES = " + str(result.mistakes))

        query += ", ".join(fields)

        query += " where RESULT_ID=" + str(result.resultId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, result):
        cursor = self.cnx.cursor()
        query = "delete from RESULT where RESULT_ID=" + str(result.resultId)
        print(query)
        cursor.execute(query)