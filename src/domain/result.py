class Result:
    def __init__(self, result_id="", athlete_id="", competition_id="", result_value="", mistakes = ""):
        self.resultId = result_id
        self.athleteId = athlete_id
        self.competitionId = competition_id
        self.resultValue = result_value
        self.mistakes = mistakes

    def __str__(self):
        return "Result:[resultId=" + self.resultId + ", athleteId=" + self.athleteId + ", competitionId=" + self.competitionId + ", resultValue=" + self.resultValue + ", mistakes=" + self.mistakes + "]"
