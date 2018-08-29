import random
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(type(lst))
#
#
# print(lst[0])
# print(lst[:3])
#
# lst[0] = 42
# print(lst)
#
# def pretty_print_lst(lst):
#     print("---------")
#     print("ID:" , id(lst))
#     print("---------")
#     for elem in lst:
#         print("Elem:" , elem)
#
# pretty_print_lst(lst)
#
# def pr_print_1(lst):
#     for i in range(len(lst)):
#         print("Elem:", lst[i])



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def multiply_list_by_n(lst, coeff):
#     for i in range(len(lst)):
#         print("Elem:", lst[i])
#         lst[i] *= coeff
#         print("Elem:", lst[i])
#
#
# multiply_list_by_n(lst, 10)


# def fill_list_by_randoms(lst, lower_bound, upper_bound):
#     for i in range(len(lst)):
#         print("Elem:", lst[i])
#         lst[i] = random.randint(lower_bound, upper_bound)
#         print("Elem:", lst[i])
#
# fill_list_by_randoms(lst, 10, 20)
# print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def fill_list_by_sum(lst):
#     sum = 0
#     for i in range(len(lst)):
#         print("Elem:", lst[i])
#         sum += lst[1]
#         # print("Elem:", lst[i])
#     return sum
#
# result = fill_list_by_sum(lst)
# print(result)


# def fill_list_by_max(lst):
#     max = lst[i]
#     for i in range(len(lst)):
#         print("Elem:", lst[i])
#         if max < lst[i]:
#             max = lst[i]
#     return max
#
# result = fill_list_by_max(lst)
# print(result)

# def fill_list_by_min(lst):
#     min = lst[1]
#     for i in range(len(lst)):
#         print("Elem:", lst[i])
#         if min > lst[i]:
#             min = lst[i]
#     return min
#
# result = fill_list_by_min(lst)
# print(result)

def fill_list_by_average(lst):
    sum = 0
    for i in range(len(lst)):
        print("Elem:", lst[i])
        sum += lst[i]

    average = sum / len(lst)
    return average

result = fill_list_by_average(lst)
print(result)

