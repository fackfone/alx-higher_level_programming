#!/usr/bin/python3
import sys
length = len(sys.argv) - 1
if (__name__ == "__main__"):
    print("{} {}{}".format(length,
          "argument" if(length == 0 or length == 1) else "arguments",
          "." if (length == 0) else ":"))
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
