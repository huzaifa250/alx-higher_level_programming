#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    kys = list(a_dictionary.keys())
    kys.sort()
    for ke in kys:
        print("{}: {}".format(ke, a_dictionary[ke]))
