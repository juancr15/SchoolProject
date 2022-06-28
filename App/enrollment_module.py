from user_module import UserModule as usrMod
from course_module import CourseModule as crMod
from Classes.enrollment import Enrollment
from validations import Validations as val

class EnrollmentModule:

    def addEnrollment():
        print("\n==== Add Enrollment ====")
        student_id=usrMod.selectStudent()[0]["student_ID"]
        course_id=crMod.selectCourse()[0]["id"]
        Enrollment.addEnrollment(student_id, course_id)

    def deleteEnrollment():
        enrollment_ID = EnrollmentModule.selectEnrollment()[0]["id"]
        Enrollment.deleteEnrollment(enrollment_ID)

    def selectEnrollment():
        while True:
                print("+++ Select Enrollment ++++")
                opEnrollment = Enrollment.listEnrollment()
                if len(opEnrollment) == 0:
                    print("No enrollment found.")
                    enrollment = []
                    break
                enrollment = Enrollment.getEnrollment(val.identification("Enter the enrollment ID: "))
                if len(enrollment):
                    break
                else:
                    print("Invalid enrollment ID. Try again.")
        return enrollment

