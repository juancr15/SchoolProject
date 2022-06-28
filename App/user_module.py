from Classes.student import *
from Classes.teacher import *
from Classes.principal import *
from validations import Validations as val

class UserModule:

    def addUser():
        """ It adds a new user according to the user's profile (Principal, Teacher or Student).
        """
        print("\n==== Add User ====")

        # Basic information of the user
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        identification = val.identification("Enter the user identification: ")
        age = val.age("Enter age: ")
        biological_sex = val.biological_sex()

        # Information depending on the user's profile
        profile = val.choice("What's the profile of this user?\n\t1. Principal\n\t2. Teacher\n\t3. Student\n\tChoice: ", 1, 4)
        if profile == 1:
            print("\n\t*** Principal")
            experience = val.choice("How many years of experience does the Principal have?: ", 0, 100)
            # Adds the Principal
            Principal(first_name, last_name, identification, age, biological_sex, experience).addPrincipal()

        elif profile == 2:
            print("\n\t***Teacher")
            ask_degree = val.choice("Does the Teacher have a degree?\n\t1. Yes\n\t2. No\n\tChoice: ", 1, 3)
            if  ask_degree == 1:
                degree = input("Enter the degree: ")
            else:
                degree = "None"
            # Asks for the Principal's ID to relate the Teacher to him
            principal_ID = UserModule.selectPrincipal()
            # Adds the Teacher
            Teacher(first_name, last_name, identification, age, biological_sex, degree).addTeacher(principal_ID)
            
        else :
            print("\n\t***Student")
            grade = val.choice("What's the grade of the student? (Between 1 and 12): ", 1, 13)
            # Asks for the Principal's ID to relate the Student to him
            principal_ID = UserModule.selectPrincipal()
            # Adds the Student
            Student(first_name, last_name, identification, age, biological_sex, grade).addStudent(principal_ID)

    def updateUser():
        """ It updates the user's information."""
        print("\n==== Update User ====")

        profile = val.choice("What's the profile of the user you want to update?\n\t1. Principal\n\t2. Teacher\n\t3. Student\n\tChoice: ", 1, 4)
        if profile == 1:
            principal_ID = UserModule.selectPrincipal()
            principal = Principal2.getPrincipal(principal_ID)

            print("----- Update Principal -----")
            basicPerson = UserModule.updatePerson(principal[0])

            if val.choice(f"Do you want to update the experience ({principal[0]['experience']})? \n\t1. Yes\n\t2. No\n\tChoice: ", 1, 3) == 1:
                experience = val.choice("How many years of experience does the Principal have?: ", 0, 100)
            else:
                experience = principal[0]['experience']

            Principal(basicPerson['first_name'], basicPerson['last_name'], 0, basicPerson['age'], 
                      basicPerson['biological_sex'], experience).updatePrincipal(principal[0]['person_ID'], 
                      principal[0]['principal_ID'])

        elif profile == 2:
            teacher = UserModule.selectTeacher()

            if len(teacher):
                print("----- Update Teacher -----")
                basicPerson = UserModule.updatePerson(teacher[0])
                
                if val.choice(f"Do you want to update {basicPerson['first_name']}'s degree ({teacher[0]['degree']})? \n\t1. Yes\n\t2. No\n\tChoice: ", 1, 3) == 1:
                    degree = input("Enter the degree: ")
                else:
                    degree = teacher[0]['degree']

                Teacher(basicPerson['first_name'], basicPerson['last_name'], 0, basicPerson['age'], 
                        basicPerson["biological_sex"], degree).updateTeacher(teacher[0]['person_ID'], 
                        teacher[0]['teacher_ID'])
        else:
            student = UserModule.selectStudent()

            if len(student):
                print("----- Update Student -----")
                basicPerson = UserModule.updatePerson(student[0])

                if val.choice(f"Do you want to update {basicPerson['first_name']}'s grade ({student[0]['grade']})? \n\t1. Yes\n\t2. No\n\tChoice: ", 1, 3) == 1:
                    grade = val.choice("What's the grade of the student? (Between 1 and 12): ", 1, 13)
                else:
                    grade = student[0]['grade']

                Student(basicPerson['first_name'], basicPerson['last_name'], 0, basicPerson['age'],
                        basicPerson["biological_sex"], grade).updateStudent(student[0]['person_ID'], 
                        student[0]['student_ID'])

    def deleteUser():
            """ It deletes a user from the database."""
            print("\n==== Delete User ====")

            profile = val.choice("What's the profile of the user you want to delete?\n\t1. Principal\n\t2. Teacher\n\t3. Student\n\tChoice: ", 1, 4)
            if profile == 1:
                principal_ID = UserModule.selectPrincipal()
                Principal2.deletePrincipal(principal_ID)

                # List of students whose Principal is missing
                chkStudent = DAO().search(f"""SELECT student.id, CONCAT(person.first_name, ' ', person.last_name) AS 'Name',
                                                    person.age AS 'Age',
                                                    student.grade AS 'Grade'
                                                FROM student
                                                INNER JOIN person ON student.person_ID = person.id 
                                                WHERE principal_ID IS NULL""")
                if chkStudent:
                    print("These are the students without a principal:")
                    print(tabulate(chkStudent, headers="keys", tablefmt="psql"))

                    # Ask if the user wants to assign a principal to the students
                    choice = val.choice("Do you want to...\n\t1. Delete all students without a principal\n\t2. Assign them one\n\t3. Do nothing\n\tChoice: ", 1, 4)

                    if choice == 1:
                        DAO().delete(f"""DELETE FROM student WHERE principal_ID IS NULL""")
                        print("All students without a principal were deleted.")
                    elif choice == 2:
                        # Assign a principal to each student
                        for student in chkStudent:
                            print(f"Assigning a principal to {student['Name']}: ")
                            DAO().update(f"""UPDATE student SET principal_ID = {UserModule.selectPrincipal()} WHERE id = {student['id']}""")
                    else:
                        print("Nothing was done.")

                # List of teachers whose Principal is missing
                chkTeacher = DAO().search(f"""SELECT teacher.id, CONCAT(person.first_name, ' ', person.last_name) AS 'Name', person.age AS 'Age'
                                                FROM teacher
                                                INNER JOIN person ON teacher.person_ID = person.id
                                                WHERE principal_ID IS NULL""")
                if chkTeacher:
                    print("These are the teachers without a principal:")
                    print(tabulate(chkTeacher, headers="keys", tablefmt="psql"))

                    # Ask if the user wants to assign a principal to the teachers
                    choice = val.choice("Do you want to...\n\t1. Delete all teachers without a principal\n\t2. Assign them one\n\t3. Do nothing\n\tChoice: ", 1, 4)
                    if choice == 1:
                        DAO().delete(f"""DELETE FROM teacher WHERE principal_ID IS NULL""")
                        print("All teachers without a principal were deleted.")
                    elif choice == 2:
                        # Assign a principal to each teacher
                        for teacher in chkTeacher:
                            print(f"Assigning a principal to {teacher['Name']}: ")
                            DAO().update(f"""UPDATE teacher SET principal_ID = {UserModule.selectPrincipal()} WHERE id = {teacher['id']}""")
                    else:
                        print("Nothing was done.")

            elif profile == 2:
                    teacher = UserModule.selectTeacher()
                    if len(teacher):
                        Teacher2.deleteTeacher(teacher[0]['teacher_ID'])
            else:
                    student = UserModule.selectStudent()
                    if len(student):
                        Student2.deleteStudent(student[0]['student_ID'])

    def updatePerson(person):
        """ It asks for the basic information of the person to update it. 
        
            Args:
                person: A dictionary with the current information of the person.

            Returns:
                A dictionary with the new information of the person.
        """
        basicInfo = dict()
        print("* If you don't want to update a field, leave it blank.")

        basicInfo['first_name'] = input(f"Enter first name ({person['first_name']}): ")

        if basicInfo['first_name'] == "":
            basicInfo['first_name'] = person['first_name']

        basicInfo['last_name'] = input(f"Enter last name ({person['last_name']}): ")
        if basicInfo['last_name'] == "":
            basicInfo['last_name'] = person['last_name']

        if val.choice(f"Do you want to update the age ({person['age']})? \n\t1. Yes\n\t2. No\n\tChoice: ", 1, 3) == 1:
            basicInfo['age'] = val.age("Enter age: ")
        else:
            basicInfo['age'] = person['age']
        
        if val.choice(f"Do you want to update the biological sex ({person['biological_sex']})? \n\t1. Yes\n\t2. No\n\tChoice: ", 1, 3) == 1:
            basicInfo['biological_sex'] = val.biological_sex()
        else:
            basicInfo['biological_sex'] = person['biological_sex']
        
        return basicInfo

    def selectPrincipal():
        """ Displays a list with the Principals in the database.

        Returns:
            int: ID of the selected principal
        """
        while True:
                print("+++ Select the Principal ++++")
                Principal2.listPrincipal()
                principal_ID = val.identification("Enter the principal ID: ")
                if len(Principal2.getPrincipal(principal_ID)):
                    break
                else:
                    print("Invalid Principal ID. Try again.")
        return principal_ID

    def selectTeacher():
        """ Displays a list with the Teachers in the database.
        
            Returns:
                Teacher: The Teacher object
        """
        while True:
                print("+++ Select the Teacher ++++")
                opTeacher = Teacher2.listTeacher()
                if not opTeacher:
                    print("No teachers found.")
                    teacher = []
                    break
                teacher = Teacher2.getTeacher(val.identification("Enter the teacher ID: "))
                if len(teacher):
                    break
                else:
                    print("Invalid Teacher ID. Try again.")
        return teacher

    def selectStudent():
        """ Displays a list with the Students in the database.

        Returns:
            int: ID of the selected student
        """
        while True:
                print("+++ Select the Student ++++")
                opStudent = Student2.listStudents()
                if len(opStudent) == 0:
                    print("No students found.")
                    student = []
                    break
                student = Student2.getStudent(val.identification("Enter the student ID: "))
                if len(student):
                    break
                else:
                    print("Invalid Student ID. Try again.")
        return student

    