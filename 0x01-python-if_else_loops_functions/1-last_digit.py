#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# To ensure the last digit of a -ive result is also -ive
if number < 0:
    saigo = -(-number % 10)
else:
    saigo = number % 10
print(f"Last digit of {number} is {saigo}", end=" ")
if saigo > 5:
    print("and is greater than 5")
elif saigo == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
