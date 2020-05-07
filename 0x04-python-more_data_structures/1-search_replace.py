#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [x for x in my_list]
    for i in range(len(new)):
        if new[i] == search:
            new[i] = replace
        else:
            pass
    else:
        return new
