#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [i for i in my_list]
    new[search - 1] = replace
    return new
