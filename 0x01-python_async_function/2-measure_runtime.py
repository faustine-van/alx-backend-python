#!/usr/bin/env python3
""" measures the total execution time
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return sort list of float random numbers"""
    # recordd start time
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    # record end time
    end_time: float = time.time()

    elapsed_time: float = end_time - start_time

    return elapsed_time / n
