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
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    sub = False
    res = 0
    counter = 0
    for i in roman_string:
        if i == "I":
            sub = True
        if sub and i != "I":
            res += base.get(i) - 2
            sub = False
        else:
            res += base.get(i)
    return res
