class Person(object):

    def __init__(self, personId, firstName, lastName, gender, emailAddress, phoneNumber, addressLine1, addressLine2, city, state, zip):
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return ("{personId: " + str(self.personId) +
                ", firstName: " + self.firstName +
                ", lastName: " + self.lastName +
                ", gender: " + self.gender +
                ", emailAddress: " + self.emailAddress + 
                ", phoneNumber: " + self.phoneNumber + 
                ", addressLine1: " + self.addressLine1 +
                ", addressLine2: " + self.addressLine2 +
                ", city: " + self.city +
                ", state: " + self.state +
                ", zip: " + self.zip +"}")
