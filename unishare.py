#Morgan Smith
#application to export images from one of our patient
#databases and import them into another

class Patient:
    def __init__(self, firstName, lastName, DoB):
        self.firstName = firstName
        self.lastName = lastName
        self.DoB = DoB

patient = Patient('test', 'test', ' 09/01/1964')

