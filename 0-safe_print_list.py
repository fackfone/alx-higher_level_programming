#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = 0
        for element in my_list:
            length += 1
        if x > length: 
            x = length
        for i in range(x):
            print(my_list[i], end="")
        print("")
        return x 
    except:
        print("Error Occured")


