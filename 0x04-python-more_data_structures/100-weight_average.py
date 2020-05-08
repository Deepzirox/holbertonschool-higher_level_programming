#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0.0
    div = []
    calc = []
    mult = 1
    suma1 = 0
    suma2 = 0
    if len(my_list) == 0:
        return 0
    else:
        for rows in my_list:
            div.append(rows[-1])
            for col in rows:
                print(col)
                mult *= col
            calc.append(mult)
            mult = 1
    suma1 = sum(calc)
    suma2 = sum(div)
    weight = suma1 / suma2
    return weight
