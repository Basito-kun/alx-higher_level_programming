#!/usr/bin/python3
for hyaku in range(100):
    if hyaku < 99:
        print("{:0=2d}, ".format(hyaku), end="")
    else:
        print("{:0=2d}".format(hyaku))
