#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    keys = sorted(keys)
    for i in keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
