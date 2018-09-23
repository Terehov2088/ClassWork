import pprint
from .person import Person


class Student(Person):
    TASKS_NUM = 37
    TEST_WEIGHTS = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]

    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = None
        self.scolarship = 1500
        self.hw_tasks = {i:0 for i in range(1, self.TASKS_NUM+1)}
        self.tests = [0]*len(self.TEST_WEIGHTS)


    def pretty_print(self):
        super().pretty_print()
        print('Scolarship:', self.scolarship)
        print('Rank:', self.total_rank())




    def accept_task(self, num_task):
        self.hw_tasks[num_task] = 1

    def accept_task_v2(self, *args):
        for arg in args:
            self.hw_tasks[arg] = 1

    def total_rank(self):
        total_rank = 0
        for key in self.hw_tasks:
            total_rank += self.hw_tasks[key]

        for i in range(len(self.tests)):
            test = self.tests[i]
            weight_coeff = self.TEST_WEIGHTS[i]
            total_rank += test * weight_coeff
        return total_rank

    def accept_test(self, num_test):
        self.tests[num_test-1] = 1








