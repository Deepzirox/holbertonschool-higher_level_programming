#!/usr/bin/python3
import calculator_1


if __name__ == '__main__':
    a = 10
    b = 5
    suma = calculator_1.add(a, b)
    resta = calculator_1.sub(a, b)
    mult = calculator_1.mul(a, b)
    division = calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, suma))
    print("{} - {} = {}".format(a, b, resta))
    print("{} * {} = {}".format(a, b, mult))
    print("{} / {} = {}".format(a, b, division))
