#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_lst = []
    sum = 0
    for num in my_list:
        if num not in new_lst:
            sum += num
            new_lst.append(num)
    return sum
