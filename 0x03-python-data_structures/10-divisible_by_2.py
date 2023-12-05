#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_lis = []
    for el in range(len(my_list)):
        if my_list[el] % 2 == 0:
            n_lis.append(True)
        else:
            n_lis.append(False)
    return n_lis
