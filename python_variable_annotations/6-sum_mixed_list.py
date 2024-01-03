#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "Adds an array of mixed types and returns a float"
    total = 0
    for x in mxd_lst:
        total += x
    return float(total)
