#!/usr/bin/env python3
"""coroutine that waits for a random delay
   between 0 and max_delay
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """return random delay between 0 and max_delay"""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
