def uniq_add(my_list=[]):
    res = 0
    tmp = []
    ocurrence = False
    for i in my_list:
        if i in tmp:
            ocurrence = True
        
        if ocurrence != True:
            res += i

        ocurrence = False
        tmp.append(i)
        
    return res
