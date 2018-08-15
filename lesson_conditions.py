# # a = 10
# # b = 0
# #
# # if b != 0:
# #     result = a / b
# #     print(result)
# # else:
# #     print('Error: Division by zero!')
# #
# # print('Finish')
# #
# #
# # b_zero = b != 0
# # #b_zero = False #false
# # print(type(b_zero))
# #
# # if b_zero:
# #     result = a / b
# #     print(result)
# # else:
# #     print('Error: Division by zero!')
#
# birth_year = 1991
#
# #if 1987 <= birth_year <= 2000:
# if birth_year > 1987 and birth_year < 2000:
#     print("I a'm millenial!")
#
# total_mileage = 90000
# year_of_ownership = 2
#
# if total_mileage > 100000 or year_of_ownership > 3:
#     print("Warranty is over!")
# else:
#     print('I\'m still fine!')
#
# def is_millenial(birth_year):
#     if 1987 <= birth_year <= 2000:
#         result = True #("I a'm millenial!")
#     else:
#         result = False #("I a'm not millenial!")
#     return result
#
# if is_millenial(birth_year):
#     print("I a'm millenial!")
#
#
# # result_1 = is_millenial(1999)
# # print(result_1)
# # # if is_millenial(birth_year):
# # #     print("I a'm millenial!")
#
#
# def warranty_check(total_mileage, year_of_ownership):
#     if not (total_mileage > 100000 or year_of_ownership > 3):
#         #result = ('I\'m still fine!')
#         return True
#     else:
#         #result = ("Warranty is over!")
#         return False
#
# if warranty_check(90000, 4):
#     print('I\'m still fine!')
# else:
#     print("Warranty is over!")
#
# def warranty_check(total_mileage, year_of_ownership):
#     if not (total_mileage > 100000 or year_of_ownership > 3):
#         result = int(5)
#     else:
#         result = int(6)
#
#     return result
#
# a = warranty_check(90000, 4)
#
# b = a*5
# print(b)
#
#
# def warranty_check(total_mileage, year_of_ownership):
#     if not (total_mileage > 100000 or year_of_ownership > 3):
#         result = ("Ne Pipec")
#     else:
#         result = ("Pipec")
#
#     return result
#
# if warranty_check(90000, 2) == str('Pipec'):
#     print("Вы должны 100к")
# else:
#     print('Тебе повезло чувак')
#

def is_millenial(birth_year):
    if 1987 <= int(birth_year) <= 2000:
        result = True
    else:
        result = False
    return result

data = input("Введите ваш возраст:")
print(data)

if is_millenial(data):
    print("I a'm millenial!")