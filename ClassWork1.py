import math

width : int = 10
length : int = 20
rectangle_square : int = width * length
print('Площаль',rectangle_square,'m2')
print('Площадь прямоугольника при ширине %d м. и длине %d м. равна %d м2' %
      (width, length, rectangle_square))

#--------------------------------------------------

cath1 : int = 3
cath2 : int = 4
hypo1 : int = (cath1**2 + cath2**2) ** 0.5
hypo2 : int = math.sqrt (cath1**2 + cath2**2)

print(hypo1)
print('\nГипотенуза треуголника с катетами %d см и %d см равна %f см' %
      (cath1, cath2, hypo2))
# задача вывод переменной
a = 0.1 + 0.1 + 0.1 - 0.3
print('\n', a)
print('\n Равно %f' % (a))

# резервируем символы перед выдачей значения
print(hypo1)
print('\n Гипотенуза треуголника с катетами %5d см и %5d см равна %10.2f см' %
      (cath1, cath2, hypo2))