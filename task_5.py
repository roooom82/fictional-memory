def print_params(a=1, b='строка', c=True):
    print(a, b, c)
values_list = [5, 'string', False]
values_dict = {'a': 4, 'b': 'my string', 'c': 1.25}
values_list_2 = [2.5, 'super string']
print_params(2)
print_params(2, 3)
print_params(2, 3, 4)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
