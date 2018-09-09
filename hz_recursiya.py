import math

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(10))


code = "print(2+2)"
eval(code)