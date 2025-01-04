# import itertools
# print(list(itertools.takewhile(lambda x: x > 0, [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] )))


import random


login = random.randint(3, 20)
password_1 = []
password_2 = []
for i in range(1, 20):
    for j in range(1, 20):
        if i < j and login % (i + j) == 0:
            password_1.append(i)
            password_2.append(j)
password = [password for x in zip(password_1, password_2) for password in x]
print(login,' - ', *password)






