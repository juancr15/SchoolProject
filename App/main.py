from Classes.student import Student
from Classes.teacher import Teacher
from Classes.principal import *
from validations import Validations as val


def mainMenu():
    flag = True
    while flag:
        print("==== Main Menu ====")
        print("Select Module:")
        print("\t1. Users")
        print("\t2. Courses")
        print("\t3. Enroll Students")
        print("\t0. Exit")
        choice = val.choice("What module do you want to access?: ", 0, 3)
        if choice == 1:
            usersMenu()
        elif choice == 2:
            coursesMenu()
        elif choice == 3:
            enrollStudents()
        else:
            flag = False

def usersMenu():
    flag = True
    while flag:
        print("==== Users Menu ====")
        print("Select action:")
        print("\t1. Add user")
        print("\t2. List user")
        print("\t3. Update user")
        print("\t4. Delete user")
        print("\t0. Exit")
        choice = val.choice("What do you want to do?: ", 0, 5)
        if choice == 1:
            addUser()
        elif choice == 2:
            print("----- List Principal -----")
            Principal2.listPrincipal()
            print("----- List of Teachers -----")
            Teacher.listTeacher()
            print("----- List of Students -----")
            Student.listStudents()
        elif choice == 3:
            updateUser()
        elif choice == 4:
            deleteUser()
        else:
            flag = False

def coursesMenu():
    flag = True
    while flag:
        print("==== Courses Menu ====")
        print("Select action:")
        print("\t1. Add course")
        print("\t2. List courses")
        print("\t3. Update course")
        print("\t4. Delete course")
        print("\t0. Exit")
        choice = val.choice("What do you want to do?: ", 0, 5)
        if choice == 1:
            addCourse()
        elif choice == 2:
            0#listCourses()
        elif choice == 3:
            updateCourse()
        elif choice == 4:
            deleteCourse()
        else:
            flag = False

def addUser():
    print("==== Add User ====")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    identification = val.identification("Enter the user identification: ") #It's not saving this attribute. Needs to be fixed.
    age = val.age("Enter age: ")
    biological_sex = val.biological_sex()
    profile = val.choice("What's the profile of this user?\n\t1. Principal\n\t2. Teacher\n\t3. Student\n\tChoice:", 1, 4)
    if profile == 1:
        print("Principal")
        experience = val.choice("How many years of experience does the Principal have?: ", 0, 100)
        Principal(first_name, last_name, identification, age, biological_sex, experience).addPrincipal()
    elif profile == 2:
        print("Teacher")
        ask_degree = val.choice("Does the Teacher have a degree?\n\t1. Yes\n\t2. No\n\tChoice:", 1, 3)
        if  ask_degree == 1:
            degree = input("Enter the degree: ")
        else:
            degree = "None"
    else :
        print("Student")
        grade = val.choice("What's the grade of the student? (Between 1 and 12): ", 1, 13)

def updateUser():
    identification = val.identification("Enter the user identification: ")

def deleteUser():
    identification = val.identification("Enter the user identification: ")

def addCourse():
    print("==== Add Course ====")
    name = input("Enter the name of the course: ")
    schedule = input("Enter the schedule of the course: ")

def updateCourse():
    course_id = val.identification("Enter the course ID: ")

def deleteCourse():
    course_id = val.identification("Enter the course ID: ")

def enrollStudents():
    student_ID = val.identification("Enter the student identification: ")
    course_ID = val.identification("Enter the course ID: ")
    return 0


mainMenu()