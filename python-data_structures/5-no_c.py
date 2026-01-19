#!/usr/bin/python3
def no_c(my_string):
    string_copy = [x for x in my_string if x != 'c' and x != 'C']

    return ''.join(string_copy)
