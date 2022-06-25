from App.Classes.person import Person

class Teacher(Person):

    def __init__(self, first_name, last_name, identification, age, biological_sex, degree):
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.degree = degree