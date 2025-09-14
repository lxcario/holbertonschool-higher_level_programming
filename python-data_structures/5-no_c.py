#!/usr/bin/python3
def no_c(my_string):
    for element in my_string:
        if element == 'c' or element == 'C':
            idx = my_string.index(element)
            my_string = my_string[:idx] + my_string[idx + 1:]
    return my_string
