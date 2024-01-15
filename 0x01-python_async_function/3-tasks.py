#!/usr/bin/env python3
""" returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """waits for a random delay for task"""
    task = asyncio.Task(wait_random(max_delay))
    return task