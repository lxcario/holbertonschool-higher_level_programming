#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    rom_to_num = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    num = 0
    length = len(roman_string)
    for i in range(length):
        current = rom_to_num.get(roman_string[i])
        if current is None:
            return None
        if i + 1 < length and rom_to_num.get(roman_string[i + 1]) > current:
            num -= current
        else:
            num += current
    return num
