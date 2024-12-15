print('module_1_5.py')
immutable_var = 2, 4, 6, 'apple', False
print(immutable_var)
# immutable_var[3] = 'orange'
# элементы кортежа нельзя заменить. Кортеж хранит ссылку на список,
# а не сам список. Если вы попытаетесь обратится к кортежу по индексу
# и заменить в нём какой-то элемент - это вызовет ошибку
# (например, ссылку на один список ссылкой на другой).
# В то время как если добавить элемент в список,
# ссылка (адрес этого списка в памяти) не измениться, следовательно,
# считается, что объект не изменился, а значит логика не нарушена -
# мы не меняли никакой элемент в кортеже.
mutable_list = [2, 4, 6, 5, 10]
mutable_list[3] = 8
mutable_list.append('copybook')
mutable_list.extend('345')
mutable_list.extend(['345'])
mutable_list.remove(10)
mutable_list.pop(1)
print(mutable_list)
print('module_1_6.py')
my_dict = {'Masha': 1775, 'Vasya': 1682,'Kolya': 1812}
print(my_dict)
print(my_dict.get('Kolya'))
print(my_dict.get('Roma'))
my_dict.update({'Roma': 1917, 'Petya': 1991})
vas = my_dict.pop('Vasya')
print(vas)
print(my_dict)
my_set = {2, 3 , 4 , 4 , 5 , 6 , 2 , 3 , 5,'red', 4.5, (5, 6, 7)}
print(my_set)
my_set.update({8,'blue'})
my_set.discard(4.5)
print(my_set)
