class Worker(object):

    def __init__(self, personId, skillDesc):
        self.personId = personId
        self.skillDesc = skillDesc

    def __str__(self):
        return ("{personId: " + str(self.personId) +
                ", skillDesc: " + self.skillDesc + "}")
