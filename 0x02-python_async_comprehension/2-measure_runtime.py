#!/usr/bin/env python3
""" Async Comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime(): - measure the total runtime
       return total time
    """
    # start record time
    start_time = time.time()
    await asyncio.gather(async_comprehension(),  async_comprehension(),
                         async_comprehension(),  async_comprehension())
    end_time = time.time()
    total_time = end_time - start_time

    return total_time
