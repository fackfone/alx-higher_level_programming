#!/usr/bin/python3
"""A square class defined by a size and
coordinates"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of2 positive integer")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        self_size = size
        return self.__size
    @property
    def position(self):
        self.__position  = position
        return self.__position
    
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value[0]) != int or type(value[1])!= int:
            raise TypeError("size must be an integer")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = value


    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if size == 0:
            print("")
        else:
            for k in range(position[0]):
                print(" ", end="")
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")


