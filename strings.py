#    example = 'Playboy'
#    print(example[0])  # Счет в строке начинается с нуля
#    print(example[-1])  #  При записи отрицательного индекса счет будет начинаться с конца
#    print(example[4:])  # срез будет происходить с указанного элемента до конечного
#    print(example[::-1])  # мы не указали границ, но уже в обратном порядке, только шаг
#    print(example[1::2])  # каждый второй символ этой строки, номер по порядку и шаг
my_string = input()
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])