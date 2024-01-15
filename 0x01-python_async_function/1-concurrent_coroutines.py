#!/usr/bin/env python3
"""coroutine that waits for a random delay
   between 0 and max_delay
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return sort list of float random numbers"""
    list_Of_float: List[float] = []
    for key in range(0, n):
        list_Of_float.append(await wait_random(max_delay))

    for i in range(0, len(list_Of_float)):
        for j in range(i + 1, len(list_Of_float)):
            if list_Of_float[i] >= list_Of_float[j]:
                temp: float = list_Of_float[i]
                list_Of_float[i] = list_Of_float[j]
                list_Of_float[j] = temp
    return list_Of_float
