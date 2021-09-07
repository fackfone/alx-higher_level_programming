#!/usr/bin/python3
for i in range(0, 100):
    if i - 10 < 0:
        print("{:0d}".format(i), end=", ")
    elif i == 99:
        print(i)
