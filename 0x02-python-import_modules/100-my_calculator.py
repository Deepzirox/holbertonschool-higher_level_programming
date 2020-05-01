#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(len(argv))
        print(argv)
    else:
        argv = argv[1:]
        if argv[1] == '+':
            sum = add(int(argv[0]), int(argv[2]))
            print("{} + {} = {}".format(argv[0], argv[2], sum))
        elif argv[1] == '-':
            su = sub(int(argv[0]), int(argv[2]))
            print("{} - {} = {}".format(argv[0], argv[2], su))
        elif argv[1] == '*':
            mult = mul(int(argv[0]), int(argv[2]))
            print("{} * {} = {}".format(argv[0], argv[2], mult))
        elif argv[1] == '/':
            di = div(int(argv[0]), int(argv[2]))
            print("{} / {} = {}".format(argv[0], argv[2], di))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
