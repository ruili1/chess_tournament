class GameView(object):

    def __init__(self, gameId, whitePlayer, blackPlayer, winner, round, status, arbiter):
        self.gameId = gameId
        self.whitePlayer = whitePlayer
        self.blackPlayer = blackPlayer
        self.winner = winner
        self.round = round
        self.status = status
        self.arbiter = arbiter

    def __str__(self):
        return ("{gameId: " + str(self.gameId) +
                ", whitePlayer: " + self.whitePlayer +
                ", blackPlayer: " + self.blackPlayer + 
                ", winner: " + self.winner + 
                ", round: " + self.round +
                ", status: " + self.status +
                ", arbiter: " + self.arbiter + "}")
