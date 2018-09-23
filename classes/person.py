class Person():


    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._email = ""
        self.__logger = None

    def pretty_print(self):
        print("========================")
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gander:', self.gender)
        print('Email:', self._email)

    def set_email(self, email):
        if not isinstance(email, str) or "@" not in email:
                print("Is invlid data!!!")
        else:
            self._email = email

    def get_email(self):
        return self._email





