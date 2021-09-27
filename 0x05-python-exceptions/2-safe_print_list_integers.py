#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        length = 0
        for element in my_list:
            length += 1
        if x > length:
            raise IndexError()
        for i in range(x):
                print(my_list[], end="")
        print("")
        return x 
    except IndexError:
        print("Error Occured")
