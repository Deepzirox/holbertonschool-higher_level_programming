#!/usr/bin/python3


for f in range(0, 10):
    for s in range(f + 1, 10):
        if f == 8 and s == 9:
            print("{:d}{:d}".format(f, s))
            break
        print("{:d}{:d}".format(f, s), end=', ')
