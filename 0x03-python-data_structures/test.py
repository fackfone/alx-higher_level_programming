#!/usr/bin/python
tuple1 = 1, 2 , 3
tuple2 = 4, 5 ,7
tuple3 = ()
for i in range(4):
    tuple3.concat(tuple1[i] + tuple2[i])
print(tuple3)
