#!/usr/bin/python3

class Square:

    def __init__(self, height = "0", width = "0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width
    
    @height.setter
    def height(self, val):
        if val.isdigit():
            self.__height = val

    @width.setter
    def width(self, val):
        if val.isdigit():
            self.__width = val

    def getArea(self):
        return int(self.__height) * int(self.__width)

def main():
    square = Square()
    height = input("Enter a height:")
    width = input("Enter a width:")
    square.height = height
    square.width = width
    print("Height: ", square.height)
    print("Width: ", square.width)
    print("Area: ", square.getArea())
main()
        

