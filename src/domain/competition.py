class Competition:
    def __init__(self, competition_id ="", name="", result_type=""):
        self.competitionId = competition_id
        self.name = name
        self.resultType = result_type

    def __str__(self):
        return "Competition:[competitionId=" + str(self.competitionId) + ", name=" + str(self.name) + ", resultType=" + str(self.resultType) + "]"
