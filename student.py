class Student:

    def __init__(self, new_firstName, new_lastName, new_slackName, new_cohortName):

        self.firstName = new_firstName
        self.lastName = new_lastName
        self.slackName = new_slackName
        self.currentCohort = new_cohortName
        self.currectExercises = []