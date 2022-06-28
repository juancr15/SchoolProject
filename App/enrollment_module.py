from user_module import UserModule as usrMod
from course_module import CourseModule as crMod
class EnrollmentModule:
    def addEnrollment():
        print("\n==== add Enrollment ====")
        student_id=usrMod.selectStudent()[0]["student_ID"]
        course_id=crMod.selectCourse()[0]["id"]
        
EnrollmentModule.addEnrollment()

