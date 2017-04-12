from domain.athlete import *


class AthleteRepository:
    def __init__(self, cnx):
        self.cnx = cnx

    def get_all(self):
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
        query = "insert into ATHLETE ("
        fields = []
        values = []
        if athlete.name:
            fields.append("NAME")
            values.append("\"" + str(athlete.name) + "\"")
        if athlete.surname:
            fields.append("SURNAME")
            values.append("\"" + str(athlete.surname) + "\"")
        if athlete.dateOfBirth:
            fields.append("DATE_OF_BIRTH")
            values.append("\"" + str(athlete.dateOfBirth) + "\"")
        if athlete.gender:
            fields.append("GENDER")
            values.append("\"" + str(athlete.gender) + "\"")
        if athlete.compNum:
            fields.append("COMP_NUM")
            values.append("\"" + str(athlete.compNum) + "\"")
        if athlete.teamId:
            fields.append("TEAM_ID")
            values.append("\"" + str(athlete.teamId) + "\"")
        if athlete.categoryId:
            fields.append("CATEGORY_ID")
            values.append("\"" + str(athlete.categoryId) + "\"")

        query += ", ".join(fields)
        query += ") values ("
        query += ", ".join(values)
        query += ");"

        print(query)

        cursor.execute(query)

    def update(self, athlete):
        cursor = self.cnx.cursor()
        query = "update ATHLETE set "

        fields = []

        if athlete.name:
            fields.append("NAME=\"" + str(athlete.name) + "\"")
        if athlete.surname:
            fields.append("SURNAME=\"" + str(athlete.surname) + "\"")
        if athlete.dateOfBirth:
            fields.append("DATE_OF_BIRTH=\"" + str(athlete.dateOfBirth) + "\"")
        if athlete.gender:
            fields.append("GENDER=\"" + str(athlete.gender) + "\"")
        if athlete.compNum:
            fields.append("COMP_NUM=" + str(athlete.compNum))
        if athlete.teamId:
            fields.append("TEAM_ID=" + str(athlete.teamId))
        if athlete.categoryId:
            fields.append("CATEGORY_ID=" + str(athlete.categoryId))

        query += ", ".join(fields)

        query += " where ATHLETE_ID=" + str(athlete.athleteId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, athlete):
        cursor = self.cnx.cursor()
        query = "delete from ATHLETE where ATHLETE_ID=" + str(athlete.athleteId)
        print(query)
        cursor.execute(query)