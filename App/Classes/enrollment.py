import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Enrollment:

    def addEnrollment(student_id,course_id):
        query = DAO().add(f"""INSERT INTO enrollment VALUES (NULL,{student_id},{course_id})""")
        print(f"New Enrollment added with ID: {query}")

    def listEnrollment():
        query = DAO().get_list(f"""SELECT enrollment.id,
                                        course.name AS 'Course Name',
                                        CONCAT(person.first_name, ' ', person.last_name) AS 'Student',
                                        course.schedule AS 'Schedule'
                                    FROM enrollment
                                    INNER JOIN student ON enrollment.student_ID = student.id
                                    INNER JOIN person ON student.person_ID = person.id
                                    INNER JOIN course ON enrollment.course_ID = course.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))
        return query['query']

    def getEnrollment(id):
        return DAO().search(f"""SELECT enrollment.id,
                                        course.name AS 'Course Name',
                                        CONCAT(person.first_name, ' ', person.last_name) AS 'Student',
                                        course.schedule AS 'Schedule'
                                    FROM enrollment
                                    INNER JOIN student ON enrollment.student_ID = student.id
                                    INNER JOIN person ON student.person_ID = person.id
                                    INNER JOIN course ON enrollment.course_ID = course.id
                                    WHERE enrollment.id = {id}""")
    
    def deleteEnrollment(id):
        DAO().delete(f"""DELETE FROM enrollment WHERE id = {id}""")
        print(f"Enrollment with ID: {id} deleted.")
