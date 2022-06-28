from .person import Person
import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Teacher(Person):

    def __init__(self, first_name, last_name, identification, age, biological_sex, degree):
        """ It initializes the class with all the arguments of the Teacher

        Args:
            first_name (string): The first name of the Teacher
            last_name (string): The  last name of the Teacher
            identification (int): The  identification of the Teacher
            age (int): The age of the Teacher
            biological_sex (char): The biological sex of the Teacher
            degree (string): The degree of the Teacher
        """
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.degree = degree

    def addTeacher(self, principal_id):
        """ Adds a new Person in the database.
            Then, it adds a new Teacher.
        
            Args:
                principal_id (int): The ID of the Principal who has the Teacher.
                self (Teacher): The Teacher object.
                
            Returns: None
        """
        newPerson = DAO().add(f"""INSERT INTO person VALUES (NULL, {self.identification}, 
                                                            '{self.first_name}', '{self.last_name}', 
                                                            {self.age}, '{self.biological_sex}')""")
        newTeacher = DAO().add(f"""INSERT INTO teacher VALUES (NULL, {newPerson}, {principal_id}, '{self.degree}')""")
        print(f"New Teacher added with ID: {newTeacher}")

    def updateTeacher(self, person_ID, teacher_ID):
        """ Updates the Teacher information in the database.
            To achieve this, it updates the table Person and then the table Teacher.
        
            Args:
                person_ID (int): The ID of the Person.
                teacher_ID (int): The ID of the Teacher.
            
            Returns: None
        """
        DAO().update(f"""UPDATE person SET first_name='{self.first_name}', last_name='{self.last_name}',
                                           age={self.age},biological_sex='{self.biological_sex}' WHERE id = {person_ID}""")
        DAO().update(f"""UPDATE teacher SET degree='{self.degree}' WHERE id = {teacher_ID};""")

class Teacher2():

    def listTeacher():
        """ Print a list with all the Teachers in the database.
        
            Args: None
            
            Returns: The result of the query.
        """
        query = DAO().get_list(query="""SELECT teacher.id, person.identification AS 'Identificacion',
                                               CONCAT(person.first_name, ' ', person.last_name) AS 'Name',
                                               person.age AS 'Age',
                                               teacher.degree AS 'Degree'
                                        FROM teacher
                                        INNER JOIN person ON teacher.person_ID = person.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))
        return query['query']

    def getTeacher(id):
        """ Returns the Teacher with the ID passed as argument.
        
            Args:
                id (int): The ID of the Teacher.
                
            Returns: A dictionary with the Teacher information.
        """
        return DAO().search(f"""SELECT teacher.id AS 'teacher_ID', person.id AS 'person_ID', 
                                       person.first_name, person.last_name, person.age, 
                                       person.biological_sex, teacher.degree
                                FROM teacher
                                INNER JOIN person ON teacher.person_ID = person.id
                                WHERE teacher.id = {id}""")

    def deleteTeacher(id):
        """ Deletes the Teacher with the ID passed as argument.
        
            Args:
                id (int): The ID of the Teacher.
            
            Returns: None
        """
        person_ID = DAO().search(f"""SELECT person_ID FROM teacher WHERE id = {id}""")[0]['person_ID']
        DAO().delete(f"""DELETE FROM teacher WHERE id = {id}""")
        DAO().delete(f"""DELETE FROM person WHERE id = {person_ID}""")
        print(f"Teacher with ID: {id} deleted")