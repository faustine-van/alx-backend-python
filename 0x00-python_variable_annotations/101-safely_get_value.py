#!/usr/bin/env python3
"""duct type"""
from typing import Union, TypeVar, Any, Mapping


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[TypeVar('T'),
                       None] = None) -> Union[Any, TypeVar('T')]:
    """Mapping TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
