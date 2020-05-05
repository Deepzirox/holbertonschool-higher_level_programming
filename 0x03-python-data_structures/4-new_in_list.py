def new_in_list(my_list, idx, element):
    new = []
    if idx < 0 or idx > len(my_list):
        return [val for val in my_list]
    else:
        new = [val for val in my_list]
        new[idx] = element
        return new
