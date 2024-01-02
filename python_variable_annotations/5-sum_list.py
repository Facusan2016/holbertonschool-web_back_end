#!/usr/bin/env python3
"""
Write a type-annotated function sum_list
which takes a list input_list of floats
as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    "Adds an array of floats and returns a float"
    total = 0
    for x in input_list:
        total += x
    return total
