#!/usr/bin/env python3
"""sum of list of floats and integers numbers"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """return sum of list of floats and int numbers
    """
    sum: float = 0
    for val in mxd_lst:
        sum += val
    return sum
