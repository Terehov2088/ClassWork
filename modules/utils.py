# modules
# + utils.py

print(__name__)

def is_even(number):
    return number % 2 == 0


def main():
    if is_even(4) == True:
        print('TEST PASSED')
    else:
        print('TEST FAILED')

    if is_even(5) == False:
        print('TEST PASSED')
    else:
        print('TEST FAILED')


if __name__ == '__main__':
    main()