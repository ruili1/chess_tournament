class TeamMemberView(object):

    def __init__(self, teamId, personId, firstName, lastName, role, skills):
        self.teamId = teamId
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName
        self.role = role
        self.skills = skills

    def __str__(self):
        return ("{teamId: " + str(self.teamId) +
                ", personId: " + self.personId +
                ", firstName: " + self.firstName + 
                ", lastName: " + self.lastName + 
                ", skills: " + self.skills+ "}")
