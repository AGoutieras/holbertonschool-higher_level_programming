#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    operator = sys.argv[2]
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))

    elif operator == '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))

    elif operator == '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))

    elif operator == '/':
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
