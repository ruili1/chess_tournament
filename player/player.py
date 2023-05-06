class Player(object):

    def __init__(self, personId, rating, ratingLevel):
        self.personId = personId
        self.rating = rating
        self.ratingLevel = ratingLevel

    def __str__(self):
        return ("{personId: " + str(self.personId) +
                ", rating: " + self.rating +
                ", ratingLevel: " + self.ratingLevel + "}")
