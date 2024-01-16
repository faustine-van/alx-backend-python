#!/usr/bin/env python3
"""generate asynchronous generator"""
import asyncio
import random


async def async_generator():
    """- coroutine will loop 10 times,
       - each time asynchronously wait 1 second,
       - yield a random number between 0 and 10.
    """
    resOfFloat = random.uniform(0, 10)
    await asyncio.sleep(1)
    for i in range(10):
        yield resOfFloat
