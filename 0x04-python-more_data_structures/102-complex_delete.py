#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    if value not in values:
        return a_dictionary
    for val in range(len(values)):
        if values[val] == value:
            a_dictionary.pop(keys[val])
    return a_dictionary
