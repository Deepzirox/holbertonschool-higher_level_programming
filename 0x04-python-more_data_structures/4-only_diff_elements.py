def only_diff_elements(set_1, set_2):
    s = set({})
    for i in set_2:
        if i not in set_1:
            s.add(i)
        for x in set_1:
            if x not in set_2:
                s.add(x)
    return s
