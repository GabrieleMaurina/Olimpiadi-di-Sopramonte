class Athlete:
    def __init__(self, athlete_id="", name="", surname="", date_of_birth="", gender="", comp_num="", team_id="", category_id=""):
        self.athleteId = athlete_id
        self.name = name
        self.surname = surname
        self.dateOfBirth = date_of_birth
        self.gender = gender
        self.compNum = comp_num
        self.categoryId = category_id
        self.teamId = team_id

    def __str__(self):
        return "Athlete:[athleteId=" + str(self.athleteId) + ", name=" + str(self.name) + ", surname=" + str(self.surname) + ", dateOfBirth=" + str(self.dateOfBirth) + ", gender=" + str(self.gender) + ", compNum=" + str(self.compNum) + ", teamId=" + str(self.teamId) + ", categoryId=" + str(self.categoryId) + "]"