class Team:
    def __init__(self, team_id="", name="", color="", comp_num_min="", comp_num_max="", race_time_male="", race_time_female=""):
        self.teamId = team_id
        self.name = name
        self.color = color
        self.compNumMin = comp_num_min
        self.compNumMax = comp_num_max
        self.raceTimeMale = race_time_male
        self.raceTimeFemale = race_time_female

    def __str__(self):
        return "Team:[teamId=" + str(self.teamId) + ", name=" + str(self.name) + ", color=" + str(self.color) + ", compNumMin=" + str(self.compNumMin) + ", compNumMax=" + str(self.compNumMax) + ", raceTimeMale=" + str(self.raceTimeMale) + ", raceTimeFemale=" + str(self.raceTimeFemale) + "]"
