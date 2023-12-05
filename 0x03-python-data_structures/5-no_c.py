#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for ch in range(len(my_string)):
        if (my_string[ch] != 'c' and my_string[ch] != 'C'):
            res += my_string[ch]
    return res
