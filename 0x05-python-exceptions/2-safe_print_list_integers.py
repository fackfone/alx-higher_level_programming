#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        length = 0
        for element in my_list:
            length += 1
        if x <= length:
            for i in range(x):
                if type(my_list[i]) == int:
                    print(my_list[i], end="")
            print("")
        else:
            raise IndexError()
        return x
    except:
        pass

