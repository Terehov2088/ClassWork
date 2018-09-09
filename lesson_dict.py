import pprint
import string
# epmty_dict = {}
#
# # initialization
en2es_dict = {'world': 'mundo',
                    'language': 'idioma',
                    'See you later': 'Hasta la vista'}
# print(en2es_dict["world"])
# en2es_dict['hi'] = 'holla'
# print(en2es_dict)
#
# en2es_dict['Hi'] = 'Holla!!!'
#
#
# # dict_planets = {'earth': 345778, 'mars': 47789, 'venus': 4679339}
# # dict_planets_2 = {'earth': (345778, 894202), 'mars': (47789, 898902), 'venus': (4679339, 238000)}
# # print(dict_planets)
#
#
# country_dict = {'Ru': ['Moscow'],
#                     'Uk': ['London'],
#                     'Cnd': ['Oslo'],
#                     'Fr' : ['Paris'],
#                     'Ua' : ['Kiev']}
# print(country_dict)
# country_dict['Ua'] = ['Lviv']
# print(country_dict)
# movies = {'Seven' : ['B.Pitt', 'K.Spacey', 'M.Freeman'],
#           'Titanic' : ['1', '2']}
# print(type(movies['Seven']))
# movies['Seven'].append('G.Paltrow')
# pprint.pprint(movies)
#
#
# country_dict['Ru'].append('Rostov'),
# country_dict['Ru'].insert(0, 'Voronej')
# pprint.pprint(country_dict)
#
# if 'Hi' in en2es_dict:
#     print('Found')
#     del en2es_dict['Hi']
# else:
#     print('Not Found')
# # pprint.pprint(en2es_dict)
#
# def pretty_print_dict(dictoinary):
#     for key in dictoinary.keys():
#         print('%s -> %s' % (key, dictoinary[key]))
#
# pretty_print_dict(en2es_dict)
#
# def pretty_print_dict_v2(dictoinary):
#     for key in dictoinary:
#         print('%s -> %s' % (key, dictoinary[key]))
#
# pretty_print_dict_v2(en2es_dict)
#
# def pretty_print_dict_v3(dictoinary):
#     for value in dictoinary.values():
#         print('?? -> %s' % value)
#
# pretty_print_dict_v4(en2es_dict)
#
# def pretty_print_dict_v4(dictoinary):
#     for key, value in dictoinary.items():
#         print('%s -> %s' % (key,value))
#
# pretty_print_dict_v4(en2es_dict)


# real examples
# person_1 = {'name':'Richard Feynman',
#             'age': 99,
#             'birth_place': 'USA',
#             'birth_date': "1918-01-01",
#             'awards':['Nobel Prize in Phisics', 'USA Science Medal']}
#
# person_2 = {'name':'Albert Einstein',
#             'age': 138,
#             'birth_place': 'Germany',
#             'birth_date': "1879-03-14",
#             'awards':['Nobel Prize in Physics', 'Planck Medal']}
#
# person_3 = {'name':'Nicola Tesla',
#             'age': 161,
#             'birth_place': 'Croatia',
#             'birth_date': "1856-07-10",
#             'awards':['Edison Medal']}
#
#
# print(person_1['name'])
# person_3['awards'].append('Pioneer')
# pprint.pprint(person_3)


# get with default
# employee_1 = {"name":"Alex", "salary": 10000, "dep": "Sales", "bonus":200}
# employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
# employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
# employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}
#
# employees = [employee_1, employee_2, employee_3, employee_4]
#
# for employee in employees:
#     employee['salary'] *= 2
#
# pprint.pprint(employees)
#
# print("======================")
#
#
# for employee in employees:
#      if 'bonus' in employee:
#          employee['bonus'] *= 2
#      else:
#          employee['bonus'] = 1000
#
# pprint.pprint(employees)
#
#
# print("======================")
#
# employees.sort(key=lambda elem: elem['salary'])
# pprint.pprint(employees)
#
# print("======================")
#
# employees.sort(key=lambda elem: elem['bonus'])
# pprint.pprint(employees)
#
# print("======================")
#
# employees.sort(key=lambda elem: elem['bonus'], reverse=True)
# pprint.pprint(employees)


# comprehension
symbols = {chr(code): 0 for code in range(ord("a"), ord("z"))}

pprint.pprint(symbols)


en2es_dict = {v: k for k, v in en2es_dict.items()}
pprint.pprint(en2es_dict)
print(en2es_dict['mundo'])


text = open('lesson_dict.py').read()
print(text)


for char in text:
    if char in symbols:
        symbols[char] += 1

pprint.pprint(symbols)


for key in sorted(symbols, key = symbols.get, reverse=True):
    print("%s -> %s" % (key,symbols[key]))