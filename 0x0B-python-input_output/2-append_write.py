#!/usr/bin/python3
"""
a module that write to text file (UTF8) and prints it to stdout
"""


def append_write(filename="", text=""):
    """ write to a file function """
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(text)
        return len(text)
