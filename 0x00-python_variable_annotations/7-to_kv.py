#!/usr/bin/env python3
"""tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple
      - string k
      -  square of v
    """
    return k, v * v
