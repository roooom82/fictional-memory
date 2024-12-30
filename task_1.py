import random

# print('Hi, PyCharm')

log_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
log_ = random.choice(log_)
password_1 = []
password_2 = []
for i in range(1, 20):
    password_1.append(i)
    for j in range(1, 20):
        if i < j and j < log_ and i != j and log_ % (i + j) == 0:
            password_2.append(j)
            password = i,j
            print(log_, password)




