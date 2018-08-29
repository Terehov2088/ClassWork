# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#


# for i in range(10):
#     for j in range(10):
#          print(i, j)


# def print_cinema_seats(rows, seats):
#     for i in range(1, rows+1):
#         print('Row %2d: ' % i, end=" ")
#         for j in range(1, seats+1):
#             print(j, end=" ")
#         print()
#
# print_cinema_seats(10, 10)



def print_mult_table(n, m):
    formatter = "%%%dd" % (len(str(n*m)))
    for i in range(1, n+1):
        for j in range(1, m+1):
            j *= i
            print(formatter % j, end=" ")
        print()


print_mult_table(10, 10)
