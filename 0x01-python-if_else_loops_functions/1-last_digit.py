#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
saigo = abs(number) % 10
if saigo > 5:
    print(f"Last digit of {number} is {saigo} and is greater than 5")
elif saigo == 0:
    print(f"Last digit of {number} is {saigo} and is 0")
else:
    print(f"Last digit of {number} is {saigo} and is less than 6 and not 0")
