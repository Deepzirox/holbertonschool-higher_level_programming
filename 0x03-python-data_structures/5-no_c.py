def no_c(my_string):
    handler = [ch for ch in my_string]
    result = ''
    for ch2 in range(len(handler)):
        if handler[ch2] != 'C' and handler[ch2] != 'c':
            result += handler[ch2]
    return result
