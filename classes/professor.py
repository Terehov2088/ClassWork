import pprint

from .person import Person

class Professor(Person):

    def __init__(self, name , age):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self._salary = 15000  # shift+f6 замена во всем коде
        self.gender = None
        self.awards = "Pioneer"

    def pretty_print(self):
        super().pretty_print()
        print('Salary:', self._salary)
        print('Awards:', self.awards)
        # print('Logger:', self.__logger)

    def set_salary(self, value):

        if isinstance(value, int):  # проверка явл ли салари интом
            if value < 0:
                print("Is invlid data!")
            else:
                self._salary = value

    def get_salary(self):
        return self._salary



