#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    argc = len(argv) - 1
    
    if len(argv) - 1 == 1:
        print("{} argument:".format(argc))

    elif len(argv) - 1 == 0:
        print("{} argument.".format(argc))

    else:
        print("{} arguments:".format(argc))

    for i, args in enumerate(argv[1:], 1):
        print("{}: {}".format(i, args))
