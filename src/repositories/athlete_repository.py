class AthleteRepository:
    def __init__(self, cursor):
        self.cursor = cursor

    def get(self, athlete):
        self.cursor.execute("select * from ATHLETE where ATHLETE_ID == " + athlete.id)
        for(id, name, surname, dateOfBirth, gender, compNum, teamId, categoryId):
            return athlete.Athlete(id, name, surname, dateOfBirth, gender, compNum, teamId, categoryId)
