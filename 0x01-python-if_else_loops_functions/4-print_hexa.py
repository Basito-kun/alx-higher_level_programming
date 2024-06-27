#!/usr/bin/python3
for suji in range(0, 99):   # to get the nos in dec
    print("{} = ".format(suji), end="")
    suji = hex(suji)    # to get the nos in hex
    print("{}".format(suji))    # I DONT GET WHY '0x' IS AUTO PRINTED THO!!!
