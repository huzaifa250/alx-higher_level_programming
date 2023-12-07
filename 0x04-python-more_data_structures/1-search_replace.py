#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Function that replaces occurrences
    of an element by another in a new list
    """
    new_list = []
    for ele in range(len(my_list)):
        if my_list[elel] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[ele])
    return new_list
