#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    argc = len(sys.argv) - 1

    if argc == 1:
        print("{} argument:".format(argc))

    elif argc == 0:
        print("{} argument.".format(argc))

    else:
        print("{} arguments:".format(argc))

    for i, args in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, args))
