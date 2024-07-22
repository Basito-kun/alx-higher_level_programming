#!/usr/bin/python3
def print_last_digit(number):
     saigo = abs(number) % 10
     print("{}".format(saigo), end="")
     return saigo
