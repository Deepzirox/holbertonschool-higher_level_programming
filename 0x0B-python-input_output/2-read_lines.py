#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename) as file:
        data = file.read()
        jumps = 0
        for i in data:
            if i == '\n':
                jumps += 1
            if jumps == nb_lines:
                break
            print(i, end='')
            


print("1 line:")
read_lines("my_file_0.txt", 1)
print("--")
print("3 lines:")
read_lines("my_file_0.txt", 3)
print("--")
print("Full content:")
read_lines("my_file_0.txt")