from domain.team import *

class TeamRepository:
    def __init__(self,cnx):
        self.cnx = cnx

    def get(self,team):
        cursor = self.cnx.cursor()
        query = "select * from TEAM"
        fields = []
        if team.teamId:
            fields.append("TEAM_ID = " + str(team.teamId))
        if team.name:
            fields.append("NAME=\"" + str(team.name) + "\"")
        if team.color:
            fields.append("COLOR=\"" + str(team.color) + "\"")
        if team.compNumMin:
            fields.append("COMP_NUM_MIN = " + str(team.compNumMin))
        if team.compNumMax:
            fields.append("COMP_NUM_MAX = " + str(team.compNumMax))
        if team.raceTimeMale:
            fields.append("RACE_TIME_MALE = " + str(team.raceTimeMale))
        if team.raceTimeFemale:
            fields.append("RACE_TIME_FEMALE = " + str(team.raceTimeFemale))

        if len(fields) > 0:
            query += " where "
        query += " and ".join(fields) + ";"
        print(query)
        cursor.execute(query)
        result = []
        for (teamId,name,color,compNumMin,compNumMax,raceTimeMale,raceTimeFemale) in cursor:
            result.append(Team(teamId,name,color,compNumMin,compNumMax,raceTimeMale,raceTimeFemale))
        return result

    def add(self, team):
        cursor = self.cnx.cursor()
        query = "insert into TEAM ("
        fields = []
        values = []
        if team.teamId:
            fields.append("TEAM_ID")
            values.append(str(team.teamId))
        if team.name:
            fields.append("NAME")
            values.append(str(team.name))
        if team.color:
            fields.append("COLOR")
            values.append(str(team.color))
        if team.compNumMin:
            fields.append("COMP_NUM_MIN")
            values.append(str(team.compNumMin))
        if team.compNumMax:
            fields.append("COMP_NUM_MAX")
            values.append(str(team.compNumMax))
        if team.raceTimeMale:
            fields.append("RACE_TIME_MALE")
            values.append(str(team.raceTimeMale))
        if team.raceTimeFemale:
            fields.append("RACE_TIME_FEMALE")
            values.append(str(team.raceTimeFemale))

        query += ", ".join(fields)
        query += ") values ("
        query += ", ".join(values)
        query += ");"

        print(query)

        cursor.execute(query)

    def update(self, team):
        cursor = self.cnx.cursor()
        query = "update TEAM set "

        fields = []

        if team.name:
            fields.append("NAME=\"" + str(team.name) + "\"")
        if team.color:
            fields.append("COLOR=\"" + str(team.color) + "\"")
        if team.compNumMin:
            fields.append("COMP_NUM_MIN = " + str(team.compNumMin))
        if team.compNumMax:
            fields.append("COMP_NUM_MAX = " + str(team.compNumMax))
        if team.raceTimeMale:
            fields.append("RACE_TIME_MALE = " + str(team.raceTimeMale))
        if team.raceTimeFemale:
            fields.append("RACE_TIME_FEMALE = " + str(team.raceTimeFemale))

        query += ", ".join(fields)

        query += " where TEAM_ID=" + str(team.teamId) + ";"

        print(query)
        cursor.execute(query)

    def remove(self, team):
        cursor = self.cnx.cursor()
        query = "delete from TEAM where TEAM_ID=" + str(team.teamId)
        print(query)
        cursor.execute(query)