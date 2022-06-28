from validations import Validations as val
from user_module import UserModule as usrMod
from Classes.course import *

class CourseModule:
    def addCourse():
        """ Adds a new course
        """
        print("\n==== Add Course ====")
        name = input("Enter the name of the course: ").capitalize()
        schedule = CourseModule.makeSchedule()
        # Select the teacher of this course
        teacher_ID = usrMod.selectTeacher()[0]['teacher_ID']

        Course(name, schedule).addCourse(teacher_ID)

    def updateCourse():
        """ Updates a course
        """

        # Select the course to update
        course = CourseModule.selectCourse()[0]
        print("* If you don't want to update a field, leave it blank.")

        name = input(f"Enter the name of the course ({course['Name']}): ").capitalize()
        if not name:
            name = course['Name']

        if val.choice(f"Do you want to change {course['Teacher']} as teacher?\n\t1. Yes\n\t2. No: ", 1, 3) == 1:
            teacher_ID = usrMod.selectTeacher()[0]['teacher_ID']
        else:
            teacher_ID = course['teacher_ID']

        if val.choice(f"Do you want to change the schedule of the course?\n\t1. Yes\n\t2. No: ", 1, 3) == 1:
            schedule = CourseModule.makeSchedule()
        else:
            schedule = course['Schedule']

        Course(name, schedule).updateCourse(course['id'], teacher_ID)
        
    def deleteCourse():
        """ Deletes a course
        """
        # Select the course to delete
        course = CourseModule.selectCourse()[0]

        Course2.deleteCourse(course['id'])

    def makeSchedule():
        """ Builds a string with the schedule of the course
        
            Returns:
                str: The schedule of the course"""

        schedule = {}
        weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        # Select the days of the week
        while True:
            day = input("Enter a day of the week: ").capitalize()

            # Validates a valid day of the week
            if day not in weekDays:
                print("The day must be one of the following: {}".format(weekDays))
                continue

            # Validates if the day is already selected
            if day in schedule:
                print("The day is already in the schedule.")
                continue

            # Select the time of the day
            while True:
                startHour = val.choice(f"Enter the start hour for {day}: ", 6, 19)
                endHour = val.choice(f"Enter the end hour {day}: ", 6, 19)

                # Validates if the time is valid
                if startHour >= endHour:
                    print("The start hour must be less than the end hour.")
                    continue
                break

            # Add the day and the hour to the schedule
            schedule[day] = str(startHour) + "-" + str(endHour)

            # Asks if the user wants to add another day to the course schedule
            if val.choice("Do you want to add another day for this course?\n\t1. Yes\n\t2. No: ", 1, 3) == 2:
                break
        
        return ', '.join(' '.join((key,val)) for (key,val) in schedule.items())

    def selectCourse():
        """ Select an existing course"""
        while True:
            print("+++ Select Course +++")
            opCourse = Course2.listCourses()
            if not opCourse:
                print("There are no courses to select.")
                course = []
                break
            course = Course2.getCourse(val.identification("Enter the course ID: "))
            if course:
                break
            else:
                print("The course ID is not valid.")
        return course