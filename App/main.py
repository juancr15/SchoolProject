from Classes.student import *
from Classes.teacher import *
from Classes.principal import *
from Classes.course import *
from Classes.enrollment import Enrollment
from validations import Validations as val
from user_module import UserModule as usrMod
from course_module import CourseModule as crsMod
from enrollment_module import EnrollmentModule as enrMod


def mainMenu():
    """ Main menu of the program """
    flag = True
    while flag:
        print("\n==== Main Menu ====")
        print("Select Module:")
        print("\t1. Users")
        print("\t2. Courses")
        print("\t3. Enrollment")
        print("\t0. Exit")
        choice = val.choice("What module do you want to access?: ", 0, 4)
        if choice == 1:
            usersMenu()
        elif choice == 2:
            coursesMenu()
        elif choice == 3:
            enrollStudents()
        else:
            flag = False

def usersMenu():
    """ Menu of the User module """
    flag = True
    while flag:
        print("\n==== Users Menu ====")
        print("Select action:")
        print("\t1. Add user")
        print("\t2. List user")
        print("\t3. Update user")
        print("\t4. Delete user")
        print("\t0. Go Back")
        choice = val.choice("What do you want to do?: ", 0, 5)
        if choice == 1:
            usrMod.addUser()
        elif choice == 2:
            print("\n----- List Principal -----")
            Principal2.listPrincipal()
            print("\n----- List of Teachers -----")
            Teacher2.listTeacher()
            print("\n----- List of Students -----")
            Student2.listStudents()
        elif choice == 3:
            usrMod.updateUser()
        elif choice == 4:
            usrMod.deleteUser()
        else:
            flag = False

def coursesMenu():
    """ Menu of the Course module"""
    flag = True
    while flag:
        print("\n==== Courses Menu ====")
        print("Select action:")
        print("\t1. Add course")
        print("\t2. List courses")
        print("\t3. Update course")
        print("\t4. Delete course")
        print("\t0. Go Back")
        choice = val.choice("What do you want to do?: ", 0, 5)
        if choice == 1:
            crsMod.addCourse()
        elif choice == 2:
            Course2.listCourses()
        elif choice == 3:
            crsMod.updateCourse()
        elif choice == 4:
            crsMod.deleteCourse()
        else:
            flag = False

def enrollStudents():
    """ Menu of the Enrollment module"""
    flag = True
    while flag:
        print("\n==== Enrollment Menu ====")
        print("Select action:")
        print("\t1. Add enrollment")
        print("\t2. List enrollment")
        print("\t3. Delete enrollment")
        print("\t0. Go Back")
        choice = val.choice("What do you want to do?: ", 0, 4)
        if choice == 1:
            enrMod.addEnrollment()
        elif choice == 2:
            Enrollment.listEnrollment()
        elif choice == 3:
            enrMod.deleteEnrollment()
        else:
            flag = False

mainMenu()