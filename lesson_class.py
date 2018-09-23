import pprint
from classes.student import Student
from classes.professor import Professor


def main():
    student1 = Student('Alice', 22)
    student2 = Student('Bob', 42)
    student3 = Student('Kate', 18)

    student3.accept_task(1)
    student3.accept_task(3)
    student3.accept_task(2)
    student3.accept_task(5)
    student1.accept_task_v2(6, 7, 8)


    student1.pretty_print()

    student2.pretty_print()

    student3.pretty_print()


    # pprint.pprint(student1.__dict__)
    # pprint.pprint(student2.__dict__)

    # student1.__dict__['name'] = 'ALICE'
    # print(student1.name)


    professor1 = Professor("Garry" , 56)
    professor1.set_email("Gert@gmail.com")
    professor1.pretty_print()
    print("======")
    # print(professor1.__logger)
    # print(professor1.get_salary())


if __name__ == '__main__':
    main()
