#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    length = len(sys.argv) - 1
    print("{} {}{}".format(length,
          "argument" if(length == 1) else "arguments",
          "." if (length == 0) else ":"))
    if length == 0:
        exit(0)
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
