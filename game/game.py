class Game(object):

    def __init__(self, gameId, whitePlayerId, blackPlayerId, winnerId, roundId, statusCd, arbiterId):
        self.gameId = gameId
        self.whitePlayerId = whitePlayerId
        self.blackPlayerId = blackPlayerId
        self.winnerId = winnerId
        self.roundId = roundId
        self.statusCd = statusCd
        self.arbiterId = arbiterId

    def __str__(self):
        return ("{gameId: " + str(self.gameId) +
                ", whitePlayerId: " + self.whitePlayerId +
                ", blackPlayerId: " + self.blackPlayerId + 
                ", winnerId: " + self.winnerId + 
                ", roundId: " + self.roundId +
                ", statusCd: " + self.statusCd +
                ", arbiterId: " + self.arbiterId + "}")
