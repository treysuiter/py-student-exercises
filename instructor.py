from nssPerson import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, new_firstName, new_lastName, new_slackName, new_cohortName, new_specialty):

        super().__init__(new_firstName, new_lastName, new_slackName, new_cohortName)
        self.specialty = new_specialty

    def assign_exercise(self, student, exercise):

        student.currectExercises.append(exercise)