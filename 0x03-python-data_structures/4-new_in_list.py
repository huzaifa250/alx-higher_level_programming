#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list.copy()  # shalow copy
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()  # copy of the org list
    else:
        my_list[idx] = element  # replace elem at index with new val
        return my_list  # modeified list
