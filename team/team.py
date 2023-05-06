class Team(object):

    def __init__(self, teamId, teamName, teamDesc):
        self.teamId = teamId
        self.teamName = teamName
        self.teamDesc = teamDesc

    def __str__(self):
        return ("{teamId: " + str(self.teamId) +
                ", teamName: " + self.teamName +
                ", teamDesc: " + self.teamDesc + "}")
