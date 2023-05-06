class WorkerView(object):

    def __init__(self, personId, firstName, lastName, skillDesc):
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName
        self.skillDesc = skillDesc

    def __str__(self):
        return ("{personId: " + str(self.personId) +
                ", firstName: " + self.firstName +
                ", lastName: " + self.lastName +
                ", skillDesc: " + self.skillDesc + "}")
