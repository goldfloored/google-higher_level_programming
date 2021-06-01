#!/usr/bin/python3
""" inheritance checking """


def is_kind_of_class(obj, a_class):
    """ function to compare object to instance """
    if isinstance(obj, a_class):
        return True
    return False
