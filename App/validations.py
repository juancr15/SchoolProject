class Validations():

    def choice(text, first, last):
        while True:
            choice = input(text)
            if not choice.isnumeric():
                print("It must be a number. Try again.")
                continue
            if int(choice) not in range(first, last):
                print("Out of limit. Try again.".format(first, last))
                continue
            else :
                break
        return int(choice)

    def age(text):
        while True:
            age = input(text)
            if not age.isnumeric():
                print("The age must be a number. Try again.")
                continue
            if int(age) == 0:
                print("The age must be greater than cero. Try again.")
                continue
            break
        return int(age)
    
    def biological_sex():
        while True:
            sex = input("Enter biological sex (M or F): ").strip().capitalize()
            if sex not in ('M', 'F'):
                print("The biological sex must be Male or Female. Try again.")
                continue
            break
        return sex

    def identification(text):
        while True:
            user_id = input(text)
            if not user_id.isnumeric():
                print("User identification must be numerical. Try again.")
                continue
            break
        return int(user_id)