class Student:

    def __init__(self, new_firstName, new_lastName, new_slackName, new_cohortName):

        self.firstName = new_firstName
        self.lastName = new_lastName
        self.slackName = new_slackName
        self.currentCohort = new_cohortName
        self.currectExercises = []

    def print_exercises(self):

        statement = ""
        i = 0
        end_index = len(self.currectExercises) - 1

        for exercise in self.currectExercises:

            if i == end_index and i > 0:
                statement += f" and {exercise.name}"

            else:
                if i == 0:
                    statement += exercise.name
                if i > 0:
                    statement += f", {exercise.name},"
            i += 1

        print(f"{self.firstName} is working on {statement}.")