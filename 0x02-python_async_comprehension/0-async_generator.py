#!/usr/bin/env python3
"""generate asynchronous generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """- coroutine will loop 10 times,
       - each time asynchronously wait 1 second,
       - yield a random number between 0 and 10.
    """
    for i in range(10):
        resOfFloat = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield resOfFloat
