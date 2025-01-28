def calculate_structure_sum(*args):
    summa = 0
    for element in args:
        if isinstance(element, str):
            summa += len(element)
        elif isinstance(element, int):
            summa += element
        elif isinstance(element, float):
            summa += element
        elif isinstance(element, bool):
            summa += element
        elif isinstance(element, list):
            summa += calculate_structure_sum(*element)
        elif isinstance(element, tuple):
            summa += calculate_structure_sum(*element)
        elif isinstance(element, set):
            summa += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            summa += calculate_structure_sum(*tuple(element.items()))
    return summa

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)