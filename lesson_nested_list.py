import random
list_2d = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 10]]
# print(list_2d)
# print(list_2d[0][0], type(list_2d[0][0]))
#
#
# list_3d = [0, [0, [1, 2, 3]]]
# print(list_3d)


def pretty_print_matrix(matrix):
    def find_max(matrix):
        max = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if max < matrix[i][j]:
                    max = matrix[i][j]
        return max

    formatter = "%%%dd" % (len(str(find_max(matrix)))+1)
    print(formatter)

    print("ID:", id(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(formatter % matrix [i][j], end="")
        print()

# pretty_print_matrix(list_2d)
#
#
# def multiply_matrix_by_n(matrix, coeff):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             matrix[i][j] *=coeff
#         print()
#
# multiply_matrix_by_n(list_2d, 10)
# pretty_print_matrix(list_2d)
#

def fill_matrix_by_randoms(matrix, lower_bound, upper_bound):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = random.randint(lower_bound, upper_bound)
# для того чтобы распечатать мы сделали универсальную функцию
# pretty_print_matrix которая вычисляет максимальный элемент и принтит

fill_matrix_by_randoms(list_2d, 1, 1000)
pretty_print_matrix(list_2d)




