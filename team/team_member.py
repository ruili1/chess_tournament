class TeamMember(object):

    def __init__(self, teamId, personId, roleCd):
        self.teamId = teamId
        self.personId = personId
        self.roleCd = roleCd

    def __str__(self):
        return ("{teamId: " + str(self.teamId) +
                ", personId: " + str(self.personId) +
                ", roleCd: " + self.roleCd + "}")
