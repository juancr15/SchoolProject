from App.Classes.person import Person

class Principal(Person):
    
    def __init__(self, first_name, last_name, identification, age, biological_sex, experience):
        super().__init__(first_name, last_name, identification, age, biological_sex)
        self.experience = experience