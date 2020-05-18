#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    intc = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            continue
        except (ValueError, TypeError):
            intc += 1
    print(' ')
    return intc
