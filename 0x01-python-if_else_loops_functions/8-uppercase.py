#!/usr/bin/python3


def uppercase(str):
    for ch in str:
        if ch != ' ':
            if ord(ch) in range(65, 90):
                ch = ord(ch)
            elif ord(ch) in range(48, 58):
                ch = ord(ch)
            else:
                ch = ord(ch) - 32
        else:
            ch = 32
        print("{}".format(chr(ch)), end='')
    print("{}".format(''))
