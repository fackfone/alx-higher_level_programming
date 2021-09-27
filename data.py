#!/usr/bin/python3
import sys
try:
    fd = open("data.txt", "r")
except FileNotFoundError:
    print("File Not Present")
else:
    print(fd.read())

    
