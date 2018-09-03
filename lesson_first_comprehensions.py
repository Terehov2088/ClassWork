import string
import random
# list comprehensions
#
# list = [i for i in range(1, 10)]
# print(list)
#
# list = [i for i in range(1, 10) if i % 2 == 0]
# print(list)
#
# list1 = [char for char in "Aaa Bbbb Dccc" if char.isupper()]
# print(list1)
#
#
#


lowers = [chr(i) for i in range(ord("а"), ord("я")+1)]
print(lowers)
print("".join(lowers))
print()
print(string.ascii_lowercase)
print()
print(string.ascii_uppercase)
print()
print(string.digits)
print()
print(max([random.randint(10,20) for _ in range(10)]))
print()
print(sum([i for i in range(101)]))
print()

text = "Создать, программу которая запрашивает у пользователя произвольную строку символов."
word_length = [len(word.strip(".,")) for word in text.split()]
print(word_length)
print('Avr. length:', sum(word_length)//len(word_length))

password_sequence1 = "".join([chr(i) for i in range(ord("a"), ord("z")+1)] + [str(i) for i in range(0, 10)])
print(password_sequence1)

password_sequence = string.ascii_uppercase + string.ascii_lowercase + string.digits
print(password_sequence)