#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


last = abs(number) % 10

if last > 5:
    msg = "and is greater than 5"

elif last == 0:
    msg = "and is zero"

else:
    msg = "and is less than 6 and not 0"

print("last digit of {} is {} {}".format(number, last, msg))
