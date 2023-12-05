#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list  # copy of the orignal list

    cop_my_list = my_list.copy()  # shallow copy
    cop_my_list[idx] = element  # replace elem index with new val
    return cop_my_list  # modeified list
