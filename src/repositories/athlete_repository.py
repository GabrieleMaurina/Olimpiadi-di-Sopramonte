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
        team_id = "\"" + str(athlete.teamId) + "\"" if athlete.teamId != "" else "NULL"
        category_id = "\"" + str(athlete.categoryId) + "\"" if athlete.categoryId != "" else "NULL"
        query = "insert into ATHLETE (NAME, SURNAME, DATE_OF_BIRTH, GENDER, COMP_NUM, TEAM_ID, CATEGORY_ID) values (\"" + str(athlete.name) + "\",\"" + str(athlete.surname) + "\",\"" + str(athlete.dateOfBirth) + "\",\"" + str(athlete.gender) + "\",\"" + str(athlete.compNum) + "\"" + "," + team_id + "," + category_id +");"
        print(query)
        cursor.execute(query)

    def update(self, athlete):
        cursor = self.cnx.cursor()
        query = "update ATHLETE set ATHLETE_ID=" + str(athlete.athleteId)

        if athlete.name:
            query += ", NAME=\"" + str(athlete.name) + "\""
        if athlete.surname:
            query += ", SURNAME=\"" + str(athlete.surname) + "\""
        if athlete.dateOfBirth:
            query += ", DATE_OF_BIRTH=\"" + str(athlete.dateOfBirth) + "\""
        if athlete.gender:
            query += ", GENDER=\"" + str(athlete.gender) + "\""
        if athlete.compNum:
            query += ", COMP_NUM=" + str(athlete.compNum)
        if athlete.teamId:
            query += ", TEAM_ID=" + str(athlete.teamId)
        if athlete.categoryId:
            query += ", CATEGORY_ID=" + str(athlete.categoryId)

        query += "where ATHLETE_ID=" + str(athlete.athleteId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, athlete):
        cursor = self.cnx.cursor()
        query = "delete from ATHLETE where ATHLETE_ID=" + str(athlete.athleteId)
        print(query)
        cursor.execute(query)