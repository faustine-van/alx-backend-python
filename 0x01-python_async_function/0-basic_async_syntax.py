#!/usr/bin/env python3
"""coroutine that waits for a random delay
   between 0 and max_delay
"""
import random


async def wait_random(max_delay: int = 10) -> float:
    """return random delay between 0 and max_delay"""
    random_float = random.uniform(0, max_delay)
    return random_float
