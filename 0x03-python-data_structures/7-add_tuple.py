#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, a2 = 0, 0
    b, b2 = 0, 0
    if len(tuple_a) >= 2:
        a, a2 = tuple_a[0:2]
    if len(tuple_b) >= 2:
        b, b2 = tuple_b[0:2]
    elif len(tuple_b) == 1:
        b = tuple_b[0]
    return (a + a2, b + b2)
