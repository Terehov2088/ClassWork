
import random

# x = 100
#
# while x > 0:
#     print('Hello World', x)
#     x -= random.randint(0, 10)


# x = 0
# while x < 100:
#     # x += 10
#     x += random.randint(0, 10)
#     print("End", x)


# def fill_truck(volume, lower_bound, upper_bound):
#     current_volume = 0
#
#     while current_volume < volume:
#         random_box = random.randint(lower_bound,upper_bound)
#         free_space = volume - current_volume
#         if free_space >= random_box:
#             current_volume +=random_box
#             print('Current volume: %d, last random box: %d' %
#                   (current_volume, random_box))
#         else:
#             print('Skipped random box: %d' % random_box)

# fill_truck(100, 1, 10)


while True:
    input_data = input('Enter data(\'q\' for exit): ')
    if input_data == 'q':
        break

    # if int(input_data) % 2 == 0:
    #     print('Even')
    # else:
    #     print('Odd')

    if not input_data.isnumeric():
        print('Invalid data')
        continue
        
    if not 0 <= int(input_data) <= 1000:
        print('Invalid data')
        continue

    if int(input_data) % 2 == 0:
        print('Even')
    else:
        print('Odd')




