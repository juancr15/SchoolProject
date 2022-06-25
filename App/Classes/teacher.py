from .person import Person
import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Teacher(Person):

    def __init__(self, first_name, last_name, identification, age, biological_sex, degree):
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.degree = degree

class Teacher():

    def listTeacher():
        query = DAO().get_list(query="""SELECT teacher.id, CONCAT(person.first_name, ' ', person.last_name) AS 'Name',
                                               person.age AS 'Age',
                                               teacher.degree AS 'Degree'
                                        FROM teacher
                                        INNER JOIN person ON teacher.person_ID = person.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))