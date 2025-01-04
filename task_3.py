calls = 0
def count_calls(calls):
    def string_info(string):
        global calls
        calls += 1
        string = len(string), string.upper(), string.lower()
        return string
    def is_contains(string, list_to_search):
        global calls
        calls += 1
        if list_to_search.count(string) > 0:
            my_list = True
        else:
            my_list = False
        return my_list

    print(string_info('banana'))
    print(string_info('apple'))
    print(string_info('snickers'))
    print(is_contains('black', ['brown','pink', 'black', 'violet']))
    print(is_contains('red', ['white', 'blue', 'orange']))
    print(is_contains('table',['apple', 'table', 'lime']))

count_calls(calls)
print(calls)
