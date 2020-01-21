# https://github.com/nashville-software-school/bangazon-llc/blob/master/book-1-orientation/chapters/STUDENT_EXERCISES_TYPES.md

from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

#Exercises
ex_chickenMonkey = Exercise("Chicken Monkey", "Python")
ex_myJournal = Exercise("My Journal", "Javascript")
ex_reactiveNutshell = Exercise("Reactive Nutshell", "React")
ex_celebrityTribute = Exercise("Celebrity Tribute", "HTML & CSS")

allExercisesArray = [ex_chickenMonkey, ex_myJournal, ex_reactiveNutshell, ex_celebrityTribute]

#Cohorts
cohort_36 = Cohort("Cohort 36")
cohort_37 = Cohort("Cohort 37")
cohort_38 = Cohort("Cohort 38")

#Students
student_treySuiter = Student("Trey", "Suiter", "treysuiter", "Cohort 36")
student_jimJam = Student("Jim", "Jam", "jimjam", "Cohort 37")
student_fredFlip = Student("Fred", "Flip", "fredflip", "Cohort 37")
student_jilJones = Student("Jil", "Jones", "jiljones", "Cohort 38")

allStudentsArray = [student_treySuiter, student_jimJam, student_fredFlip, student_jilJones]

#Instructors
instructor_joeShep = Instructor("Joe", "Sheppard", "joeshep", "Cohort 36", "Board Games")
instructor_jisieDavid = Instructor("Jisie", "David", "jisiedavid", "Cohort 37", "Ping Pong" )
instructor_kristenNorris = Instructor("Kristen", "Norris", "kristen_norris", "Cohort 37", "Volleyball")
instruct_RoseW = Instructor("Rose", "Wzuoutki", "roseW", "Cohort 38", "Billiards")

#Assigning exercises
instructor_joeShep.assign_exercise(student_treySuiter, ex_chickenMonkey)
instructor_joeShep.assign_exercise(student_treySuiter, ex_myJournal)
instructor_joeShep.assign_exercise(student_treySuiter, ex_reactiveNutshell)
instructor_joeShep.assign_exercise(student_treySuiter, ex_celebrityTribute)

instructor_jisieDavid.assign_exercise(student_jimJam, ex_myJournal)
instructor_jisieDavid.assign_exercise(student_jimJam, ex_celebrityTribute)
instructor_jisieDavid.assign_exercise(student_jimJam, ex_chickenMonkey)

instructor_kristenNorris.assign_exercise(student_fredFlip, ex_celebrityTribute)
instructor_kristenNorris.assign_exercise(student_fredFlip, ex_reactiveNutshell)

instruct_RoseW.assign_exercise(student_jilJones, ex_reactiveNutshell)

for student in allStudentsArray:

    student.print_exercises()