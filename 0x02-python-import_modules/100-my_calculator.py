#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    argc = len(sys.argv)
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if (op == "+"):
        print("{} + {} = {}".format(a, b, add(a, b)))
        sys.exit(0)
    elif (op == "-"):
        print("{} - {} = {}".format(a, b, sub(a, b)))
        sys.exit(0)
    elif (op == "*"):
        print("{} * {} = {}".format(a, b, mul(a, b)))
        sys.exit(0)
    elif (op == "/"):
        print("{} / {} = {}".format(a, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
