s='TiliWili'
print(type(s))
print(s)
s4 = """
line 1
line 2
line 3
"""
print(s4)

print(s4.count('e'))


s10 = 'Lesson2'

print(s10.lower())

path = 'C:\\temp\\new folder\\lesson_3'
print(path)
path1 = r'C:\temp\new folder\lesson_3'
print(path1)
"""символ r убирает специальность сиволов и 
говорит питону трактовать их как обычный текст
"""
#---------------------------------------
s7 = "python"

"""
"Python"
Index+ 0 1 2 3 4 5
Index- -1 -2 -3 -4 -5 -6
"""

print(s7[0],s7[-6].title())

print(s7[2:5])
print(s7[-5:2].title())

s9 = 'ababababa'
print(s9[::2]) #переход через 1 символ
print(s9[::-1]) #разворот строки


#---------------------

timestamp = "18:13:42"
hours = int(timestamp[0:2])
minute = int (timestamp[3:5])
second = int (timestamp[6:])

print('Часы = %d , минуты = %d , секунды = %d ' % (hours, minute, second))


total_seconds = hours * (60*60) + minute*60 + second
print("Прошло сукунд с начала дня:", total_seconds)

timestamp_1st = timestamp.split(":")
print(timestamp_1st)




timestamp = "18:3:42"

timestamp_1st = timestamp.split(":")
print(type(timestamp_1st))
print(timestamp_1st[0])
print(timestamp_1st[1])
print(timestamp_1st[2])

#--------------------------

hours = int(timestamp_1st[0])
minute = int (timestamp_1st[1])
second = int (timestamp_1st[2])
total_seconds = hours * (60*60) + minute*60 + second
print("Прошло сукунд с начала дня:", total_seconds)

#--------------

email = 'musk@spacex.com'
email_name = email.split('@')[0]
print(email_name)
email_name_idx = email.find('@')
email_name = email[:email_name_idx]
print(email_name)