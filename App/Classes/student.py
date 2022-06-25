from App.Classes.person import Person

class Student(Person):

    def __init__(self, first_name, last_name, identification, age, biological_sex, grade):
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.grade = grade