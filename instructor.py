class Instructor:

    def __init__(self, new_firstName, new_lastName, new_slackName, new_currentCohort, new_specialty):

        self.firstName = new_firstName
        self.lastName = new_lastName
        self.slackName = new_slackName
        self.currectCohort = new_currentCohort
        self.specialty = new_specialty

    def assign_exercise(self, student, exercise):

        student.currectExercises.append(exercise)