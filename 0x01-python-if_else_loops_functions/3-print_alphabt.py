#!/usr/bin/python3
for tsu in range(97, 123):
    tsu = chr(tsu)
    if tsu not in "q" "e":
        print("{}".format(tsu), end="")
