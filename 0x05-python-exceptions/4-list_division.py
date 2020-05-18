#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    div = 0
    for n in range(list_length):
        try:
            div = my_list_1[n] / my_list_2[n]
            res.append(div)
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            res.append(0)
        except TypeError:
            print("{}".format("wrong type"))
            res.append(0)
        except IndexError:
            print("{}".format("out of range"))
            res.append(0)
        finally:
            continue
    return res
