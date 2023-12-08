#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        my_lst = list(a_dictionary.keys())
        mx_key = None
        mx_val = 0
        for k, v in a_dictionary.items():
            if v > mx_val:
                mx_val = v
                mx_key = k

        return my_lst
