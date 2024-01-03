#!/usr/bin/env python3
"""
Annotate the below function’s parameters
and return values with the appropriate types
"""

from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    "Returns the length of the elements in lst"
    return [(i, len(i)) for i in lst]
