#!/usr/bin/python3
def roman_to_int(roman_string):
    base = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    res = 0
    for i in range(len(roman_string)):
        res += base.get(roman_string[i])
        if roman_string[i - 1] == 'I' and i != 0:
            res -= 2
    return res
