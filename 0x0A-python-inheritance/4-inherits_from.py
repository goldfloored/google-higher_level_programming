#!/usr/bin/python3
""" verification module """


def inherits_from(obj, a_class):
    """ function to verif subclass """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
