class Round(object):

    def __init__(self, roundId, tournamentId, startTime, ratingLevel):
        self.roundId = roundId
        self.tournamentId = tournamentId
        self.startTime = startTime
        self.ratingLevel = ratingLevel

    def __str__(self):
        return ("{roundId: " + str(self.roundId) +
                ", tournamentId: " + self.tournamentId +
                ", startTime: " + self.startTime + 
                ", ratingLevel: " + self.ratingLevel + "}")
