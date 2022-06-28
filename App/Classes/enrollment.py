import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Enrollment:
    def enrollment(student_id,course_id):
        query=DAO().add(f"""INSERT INTO enrollment VALUES (NULL,{student_id},{course_id})""")
