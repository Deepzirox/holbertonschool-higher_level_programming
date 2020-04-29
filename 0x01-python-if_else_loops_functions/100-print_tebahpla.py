#!/usr/bin/python3


counter = 2
handler = 0
for ch in range(122, 96, -1):
    if counter % 2 == 0:
        handler = 0
    else:
        handler = 32
    print("{}".format(chr(ch - handler)), end='')
    counter += 1
