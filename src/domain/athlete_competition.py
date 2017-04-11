class AthleteCompetition:
    def __init__(self, athlete_id="", competition_id="", placement="", score=""):
        self.athleteId = athlete_id
        self.competitionId = competition_id
        self.placement = placement
        self.score = score

    def __str__(self):
        return "AthleteCompetition:[athleteId=" + self.athleteId + ", competitionId=" + self.competitionId + ", placement=" + self.placement + ", score=" + self.score + "]"
