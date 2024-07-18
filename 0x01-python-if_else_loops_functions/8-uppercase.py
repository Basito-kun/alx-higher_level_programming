def uppercase(str):
    for lett in str:
        if ord(lett) >= 97 and ord(lett) <= 122:
            # converting lower to upper case by subtracting 32 from ASCII value
            caps = chr(ord(lett) - 32)
        else:
            caps = lett
        print("{}".format(caps), end="")
    print()
