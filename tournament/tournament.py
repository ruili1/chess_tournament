class Tournament(object):

    def __init__(self, tournamentId, tournamentName, addressLine1, addressLine2, city, state, zip):
        self.tournamentId = tournamentId
        self.tournamentName = tournamentName
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return ("{tournamentId: " + str(self.tournamentId) +
                ", tournamentName: " + self.tournamentName +
                ", addressLine1: " + self.addressLine1 + 
                ", addressLine2: " + self.addressLine2 + 
                ", city: " + self.city + 
                ", state: " + self.state +
                ", zip: " + self.zip + "}")
