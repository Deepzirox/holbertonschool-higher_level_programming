#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    keys = a_dictionary.keys()
    for i in keys:
        new.update({i: a_dictionary[i] * 2})
    return new
