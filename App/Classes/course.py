import sys
sys.path.append(".")
from DB.connection import DAO
from tabulate import tabulate

class Course():

    def __init__(self, name, schedule):
        """ It initializes the class with all the arguments of the Course

        Args:
            name (string): Name of the Course
            schedule (string): Schedule of the Course
        """
        self.name = name
        self.schedule = schedule

    def addCourse(self, teacher_ID):
        """ Adds a new Course to the database.
        
            Args:
                self (Course): The Course object.
                teacher_ID (int): The ID of the Teacher.
        """
        course_ID = DAO().add(f"""INSERT INTO course VALUES (NULL, {teacher_ID}, '{self.name}', '{self.schedule}')""")
        print(f"New Course added with ID: {course_ID}")
    
    def updateCourse(self, course_ID, teacher_ID):
        """ Updates the Course information in the database.
        
            Args:
                course_ID (int): The ID of the Course.
                teacher_ID (int): The ID of the Teacher.
                self (Course): The Course object.
            """
        DAO().update(f"""UPDATE course SET teacher_ID={teacher_ID}, name='{self.name}', schedule='{self.schedule}'
                         WHERE id = {course_ID}""")
    
class Course2:

    def listCourses():
        """List all the Courses in the database.
        
            Args: None
        """
        query = DAO().get_list(f"""SELECT course.id, course.name AS 'Course Name', 
                                          CONCAT(person.first_name, ' ', person.last_name) AS 'Teacher Name', 
                                          course.schedule AS 'Schedule'
                                    FROM course
                                    INNER JOIN teacher ON course.teacher_ID = teacher.id
                                    INNER JOIN person ON teacher.person_ID = person.id""")
        print(tabulate(query['query'], headers=query['headers'], tablefmt='psql'))
        return query['query']
    
    def getCourse(id):
        """ Get the Course information from the database.
        
            Args:
                id (int): The ID of the Course.
                
            Returns: The result of the query.
        """
        return DAO().search(f"""SELECT course.id, course.name AS 'Name',
                                        course.teacher_ID,
                                        CONCAT(person.first_name, ' ', person.last_name) AS 'Teacher', 
                                        course.schedule AS 'Schedule'
                                FROM course
                                INNER JOIN teacher ON course.teacher_ID = teacher.id
                                INNER JOIN person ON teacher.person_ID = person.id
                                WHERE course.id = {id}""")
    
    def deleteCourse(id):
        """ Delete the Course from the database.
        
            Args:
                id (int): The ID of the Course.
        """
        DAO().delete(f"""DELETE FROM course WHERE id = {id}""")
        print(f"Course with ID {id} deleted.")