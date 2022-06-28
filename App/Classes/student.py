from .person import Person
import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Student(Person):

    def __init__(self, first_name, last_name, identification, age, biological_sex, grade):
        """It initializes the class with all the arguments of the Student

        Args:
            first_name (string): The first name of the Student
            last_name (string): The last name of the Student
            identification (int): The identification of the Student
            age (int): The age of the Student
            biological_sex (char): The biological sex of the Student
            grade (int): The grade where the student is in
        """
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.grade = grade

    def addStudent(self, principal_id):
        """ Adds a new Student to the database.
        
            Args:
                principal_id (int): The ID of the Principal who is adding the Student.
                self (Student): The Student object.
                
            Returns: None
        """
        newPerson = DAO().add(f"""INSERT INTO person VALUES (NULL, {self.identification},
                                                            '{self.first_name}', '{self.last_name}', 
                                                            {self.age}, '{self.biological_sex}')""")
        newStudent = DAO().add(f"""INSERT INTO student VALUES (NULL, {newPerson}, {principal_id}, {self.grade})""")
        print(f"New Student added with ID: {newStudent}")

    def updateStudent(self, person_ID, student_ID):
        """ Updates the Student information in the database.
            First, it updates the table Person and then the table Student.
        
            Args:
                person_ID (int): The ID of the Person.
                student_ID (int): The ID of the Student.
                
            Returns: None
        """
        DAO().update(f"""UPDATE person SET first_name='{self.first_name}', last_name='{self.last_name}',
                                           age={self.age},biological_sex='{self.biological_sex}' 
                         WHERE id = {person_ID}""")
                         
        DAO().update(f"""UPDATE student SET grade={self.grade}
                         WHERE id = {student_ID};""")

class Student2():
    
    def listStudents():
        """ Print a list with all the Students in the database.
        
            Args: None
            
            Returns: The result of the query
        """
        query = DAO().get_list(query="""SELECT student.id, person.identification AS 'Identificacion',
                                               CONCAT(person.first_name, ' ', person.last_name) AS 'Name',
                                               person.age AS 'Age',
                                               student.grade AS 'Grade'
                                        FROM student
                                        INNER JOIN person ON student.person_ID = person.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))
        return query['query']

    def getStudent(id):
        """ Returns the Student with the ID passed as argument.
        
            Args:
                id (int): The ID of the Student.
                
            Returns: A dictionary with the Student information."""
        return DAO().search(f"""SELECT student.id AS 'student_ID', person.id AS 'person_ID', 
                                       person.first_name, person.last_name, person.age, 
                                       person.biological_sex, student.grade
                                FROM student
                                INNER JOIN person ON student.person_ID = person.id
                                WHERE student.id = {id}""")

    def deleteStudent(id):
        """ Deletes the Student with the ID passed as argument.
        
            Args:
                id (int): The ID of the Student.
                
            Returns: None"""
        person_ID = DAO().search(f"""SELECT person_ID FROM student WHERE id = {id}""")[0]['person_ID']
        DAO().delete(f"""DELETE FROM student WHERE id = {id}""")
        DAO().delete(f"""DELETE FROM person WHERE id = {person_ID}""")
        print(f"Student with ID: {id} deleted")

   


