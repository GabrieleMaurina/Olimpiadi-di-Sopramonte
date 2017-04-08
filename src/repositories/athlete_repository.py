from domain.athlete import *

class AthleteRepository:
    def __init__(self, cnx):
        self.cnx = cnx

    def getAll(self):
        cursor = self.cnx.cursor()
        query = "select * from ATHLETE;"
        print(query)
        cursor.execute(query)
        result = []
        for (id, name, surname, dateOfBirth, gender, compNum, teamId, categoryId) in cursor:
            result.append(Athlete(id, name, surname, dateOfBirth, gender, compNum, teamId, categoryId))
        return result


    def get(self, athlete):
        cursor = self.cnx.cursor()
        query = "select * from ATHLETE where ATHLETE_ID = " + str(athlete.id) + ";"
        print(query)
        cursor.execute(query)
        for (id, name, surname, dateOfBirth, gender, compNum, teamId, categoryId) in cursor:
            return Athlete(id, name, surname, dateOfBirth, gender, compNum, teamId, categoryId)


    def add(self, athlete):
        cursor = self.cnx.cursor()
        teamId = "\"" + athlete.teamId + "\"" if athlete.teamId != "" else "NULL"
        categoryId = "\"" + athlete.categoryId + "\"" if athlete.categoryId != "" else "NULL"
        query = "insert into ATHLETE (NAME, SURNAME, DATE_OF_BIRTH, GENDER, COMP_NUM, TEAM_ID, CATEGORY_ID) values (\"" + athlete.name + "\",\"" + athlete.surname + "\",\"" + athlete.dateOfBirth + "\",\"" + athlete.gender + "\",\"" + str(athlete.compNum) + "\"" + "," + teamId + "," + categoryId +");"
        print(query)
        cursor.execute(query)