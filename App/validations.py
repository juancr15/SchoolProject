class Validations():

    def choice(text, first, last):
        """ It validates the choice of the user.

        Args:
            text (string): The text to be displayed.
            first (int): The first option of the menu.
            last (int): The last option of the menu plus one.

        Returns:
            int: The choice of the user.
        """
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
        """ It validates the age of the user.

        Args:
            text (string): The text to be displayed.

        Returns:
            int: The age of the user.
        """
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
        """It asks for the biological sex of the person

        Returns:
            char: The biological sex
        """
        while True:
            sex = input("Enter biological sex (M or F): ").strip().capitalize()
            if sex not in ('M', 'F'):
                print("The biological sex must be Male or Female. Try again.")
                continue
            break
        return sex

    def identification(text):
        """It validates the id given by the user

        Args:
            text (string): The text displayed

        Returns:
            int: The id
        """
        while True:
            user_id = input(text)
            if not user_id.isnumeric():
                print("User identification must be numerical. Try again.")
                continue
            break
        return int(user_id)