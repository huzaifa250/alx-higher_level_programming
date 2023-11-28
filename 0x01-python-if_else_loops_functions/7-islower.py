#!/usr/bin/python3

def islower(c):
    """function check for lowercase letter
    ord returns the ASCII value of the character"""
    if ord(c) in range(97, 123):
        return True
    else:
        return False
