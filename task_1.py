# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# positive =[]
# index = 0
# while index < len(my_list):
#     if my_list[index] < 0:
#         break
#     positive.append(my_list[index])
#     index += 1
# print(positive)
from gc import get_threshold


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    return matrix
result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)











