#!/usr/bin/python3
""" module to compare object to instance """


def is_same_class(obj, a_class):
    """ function to compare object to instance """
    if type(obj) is a_class:
        return True
    else:
        return False
