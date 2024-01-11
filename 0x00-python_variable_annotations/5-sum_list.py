#!/usr/bin/env python3
"""sum of list of floats numbers"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of list of floats number
    """
    sum: float = 0
    for val in input_list:
        sum += val
    return sum
