#!/usr/bin/python3
"""
convert json representation to string
"""
import json


def save_to_json_file(my_obj, filename):
    """ save to json file """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
