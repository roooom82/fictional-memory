def get_multiplied_digits(number):
    str_number = str(number)

    if len(str_number) == 1:
        first = int(str_number[0])
        if first == 0:
        # str_number = str_number.replace('0', '4')
            return first + 1
        else:
            return first
    elif len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(402030)
print (result)