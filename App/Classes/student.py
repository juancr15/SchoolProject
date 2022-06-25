from .person import Person
import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Student(Person):

    def __init__(self, first_name, last_name, identification, age, biological_sex, grade):
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.grade = grade

class Student():
    
    def listStudents():
        query = DAO().get_list(query="""SELECT student.id, CONCAT(person.first_name, ' ', person.last_name) AS 'Name',
                                               person.age AS 'Age',
                                               student.grade AS 'Grade'
                                        FROM student
                                        INNER JOIN person ON student.person_ID = person.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))