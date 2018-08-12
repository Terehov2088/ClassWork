#def <func_name>(<param_list>):
#    <func_body_line1>
#    <func_body_line2>
#    <func_body_lineN>
import math

def print_hello():
    print('Hello')

print_hello()
print_hello()
print_hello()
print_hello()

def print_hello_name(name):
    print('Hello, %s!' % name)

print_hello_name('Vladimir')

def rectangle_square(width, height):
    rectangle_square: int = width * height
    print('Площаль', rectangle_square, 'm2')
    print('Площадь прямоугольника при ширине %d м. и длине %d м. равна %d м2' %
          (width, height, rectangle_square))
    return(rectangle_square)

result2 = rectangle_square(2, 10)
print("Result:", result2)


def square_circle(radius):
    square_circle_1 = math.pi * (radius**2)
    return(square_circle_1)

print(square_circle(2))

def value_sphere(radius):
    value_sphere_1 = (4 / 3) * math.pi * math.pow(radius, 3)
    return(value_sphere_1)

print(value_sphere(2))

# cels = float(input('Укажите градусы по цельсию:'))
# def cels2faren(degrees):
#     cels2faren_1 = (degrees * 9/5) + 32
#     return(cels2faren_1)


print(cels2faren(cels))


def cels2faren_and_kelvins(degreese):
    result_cels = degreese * 9 / 5 +32
    result_kelvins = degreese + 273.15
    return result_cels, result_kelvins

results5, results6 = cels2faren_and_kelvins(36.6)
print('Results: %.2f, %.2f' % (results5, results6))