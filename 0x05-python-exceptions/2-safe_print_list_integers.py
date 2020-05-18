#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    intc = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            intc += 1
            continue
        except (ValueError, TypeError):
            pass
    print(' ')
    return intc
