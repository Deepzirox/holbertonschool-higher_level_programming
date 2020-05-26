#!/usr/bin/python3
i = 0
def magic_string():
    return "Holberton " * (i += 1)

for i in range(10):
    print(magic_string())