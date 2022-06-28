from .person import Person
import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Principal(Person):
    
    def __init__(self, first_name, last_name, identification, age, biological_sex, experience):
        """ It initializes the class with all the arguments of the Principal

        Args:
            first_name (string): The first name of the Principal
            last_name (string): The last name of the Principal
            identification (int): The identification of the Principal
            age (int): The age of the Principal
            biological_sex (char): The biological sex of the Principal
            experience (int): The years of experience that the Principal has
        """
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.experience = experience

    def addPrincipal(self):
        """ Adds a new Principal to the database.
        
            Args: 
                self (Principal): The Principal object.
            
            Returns: None"""
        newPerson = DAO().add(f"""INSERT INTO person VALUES (NULL, {self.identification},
                                                            '{self.first_name}', '{self.last_name}', 
                                                            {self.age}, '{self.biological_sex}')""")
        newPrincipal = DAO().add(f"""INSERT INTO principal VALUES (NULL, {newPerson}, {self.experience})""")
        print(f"New Principal added with ID: {newPrincipal}")

    def updatePrincipal(self, person_ID, principal_ID):
        """ Updates the Principal information in the database.
            First, it updates the table Person and then the table Principal.
            
            Args:
                person_ID (int): The ID of the Person.
                principal_ID (int): The ID of the Principal.
                
            Returns: None
        """
        DAO().update(f"""UPDATE person SET first_name='{self.first_name}', last_name='{self.last_name}',
                                           age={self.age},biological_sex='{self.biological_sex}' 
                         WHERE id = {person_ID}""")

        DAO().update(f"""UPDATE principal SET experience={self.experience} 
                         WHERE id = {principal_ID};""")


class Principal2():

    def listPrincipal():
        """ Print a list with all the Principals in the database.
        
            Args: None
            
            Returns: None
        """
        query = DAO().get_list(query="""SELECT principal.id, person.identification AS 'Identificacion',
                                               CONCAT(person.first_name, ' ', person.last_name) AS 'Name',
                                               person.age AS 'Age',
                                               principal.experience AS 'Experience'
                                        FROM principal
                                        INNER JOIN person ON principal.person_ID = person.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))

    def getPrincipal(id):
        """ Returns the Principal with the ID passed as argument.

            Args:
                id (int): The ID of the Principal.

            Returns: A dictionary with the Principal information.
        """
        return DAO().search(f"""SELECT principal.id AS 'principal_ID', person.id AS 'person_ID', 
                                       person.first_name, person.last_name, person.age, 
                                       person.biological_sex, principal.experience
                                FROM principal
                                INNER JOIN person ON principal.person_ID = person.id
                                WHERE principal.id = {id}""")

    def deletePrincipal(id):
        """ Deletes the Principal with the ID passed as argument.
        
            Args:
                id (int): The ID of the Principal.
                
            Returns: None
        """
        person_ID = DAO().search(f"""SELECT person_ID FROM principal WHERE id = {id}""")[0]['person_ID']
        DAO().delete(f"""DELETE FROM principal WHERE id = {id}""")
        DAO().delete(f"""DELETE FROM person WHERE id = {person_ID}""")
        print(f"Principal with ID: {id} deleted")