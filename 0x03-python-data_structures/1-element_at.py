#!/usr/bin/python3
def element_at(my_list, idx):
    if str(idx).isnumeric() == False:
        return None
    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]

