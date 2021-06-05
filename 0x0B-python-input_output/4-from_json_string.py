#!/usr/bin/python3
"""
convert json representation to string
"""
import json


def from_json_string(my_str):
    """ function return string from json """
    return json.loads(my_str)
