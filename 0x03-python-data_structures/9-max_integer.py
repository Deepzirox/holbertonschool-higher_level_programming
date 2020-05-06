#!/usr/bin/python3
def max_integer(my_list=[]):
    max_n = 0
    if len(my_list) == 0:
        return None
    else:
        max_n = my_list[0]
        for n in my_list:
            if n > max_n:
                max_n = n
    return max_n
