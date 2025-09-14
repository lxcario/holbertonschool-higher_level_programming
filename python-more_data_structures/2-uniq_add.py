#!/usr/bin/python3
def uniq_add(my_list=[]):
    elements = []
    sum = 0
    for element in my_list:
        if element not in elements:
            elements.append(element)
            sum += element
    return sum
