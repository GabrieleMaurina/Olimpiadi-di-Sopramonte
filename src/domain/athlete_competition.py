class AthleteCompetition:
    def __init__(self, athlete_id="", competition_id="", placement="", score=""):
        self.athleteId = athlete_id
        self.competitionId = competition_id
        self.placement = placement
        self.score = score

    def __str__(self):
        return "AthleteCompetition:[athleteId=" + str(self.athleteId) + ", competitionId=" + str(self.competitionId) + ", placement=" + str(self.placement) + ", score=" + str(self.score) + "]"
