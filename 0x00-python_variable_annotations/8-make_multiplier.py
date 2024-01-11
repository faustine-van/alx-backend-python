#!/usr/bin/env python3
"""functions callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float
    by multiplier.
    """
    def multiplier(x: float) -> float:
        return x * x
    return multiplier
