from .person import Person
import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Principal(Person):
    
    def __init__(self, first_name, last_name, identification, age, biological_sex, experience):
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.experience = experience

    def addPrincipal(self):
        newPerson = DAO().add(f"""INSERT INTO person VALUES (NULL, '{self.first_name}', '{self.last_name}', {self.age}, '{self.biological_sex}')""")
        newPrincipal = DAO().add(f"""INSERT INTO principal VALUES (NULL, {newPerson}, {self.experience})""")
        print(f"New Principal added with ID: {newPrincipal}")


class Principal2():

    def listPrincipal():
        query = DAO().get_list(query="""SELECT principal.id, CONCAT(person.first_name, ' ', person.last_name) AS 'Name',
                                               person.age AS 'Age',
                                               principal.experience AS 'Experience'
                                        FROM principal
                                        INNER JOIN person ON principal.person_ID = person.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))