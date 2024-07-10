#!/usr/bin/python3
def islower(c):
    """Testing for lower and upper case digits
    using ord() to select lower xter range"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
