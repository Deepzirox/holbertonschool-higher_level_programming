#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bools = []
    for n in my_list:
        if n % 2 == 0:
            bools.append(True)
        else:
            bools.append(False)
    return bools
