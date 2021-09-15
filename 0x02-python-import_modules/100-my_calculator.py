#!/usr/bin/python3
def main(argv):
    operation = {'+': add, '-': sub, '*': mul, '/': div}
    length = len(argv) - 1
    if length != 3:
        print("Usage: {:s}"
              " <a> <operator> <b>".format(argv[0]))
        exit(1)
    op = argv[2]
    if (op not in '+*/-'):
        print("{:s}".format("Unknown operator."
              "Available operators: +, -, * and /"))
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, operation[op](a, b)))

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    main(argv)
