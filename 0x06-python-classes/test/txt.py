#!/usr/bin/python3
class Robot(object):
    pass
x = Robot()
y = Robot()
x.brand = "HX-YV5K3"

y.brand = "KK-IVKF3"

print(Robot.__dict__)
print(x.__dict__)
print(y.__dict__)
