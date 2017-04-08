class Athlete:
    def __init__(self, id="", name="", surname="", date_of_birth="", gender="", comp_num="", category_id="", team_id=""):
        self.id = id
        self.name = name
        self.surname = surname
        self.dateOfBirth = date_of_birth
        self.gender = gender
        self.compNum = comp_num
        self.categoryId = category_id
        self.teamId = team_id

    def __str__(self):
        return "ID=" + str(self.id) + " NAME=" + str(self.name) + " SURNAME=" + str(self.surname) + " DATE_OF_BIRTH=" + str(self.dateOfBirth) + " GENDER=" + str(self.gender) + " COMP_NUM=" + str(self.compNum) + " TEAM_ID=" + str(self.teamId) + " CATEGORY_ID=" + str(self.categoryId)
