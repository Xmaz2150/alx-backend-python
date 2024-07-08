#!/usr/bin/env python3

"""
asynchronous `wait_random` coroutine
modul
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for random seconds between 0 and `max_delay`
    returns time waited
    """
    wait: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait)

    return wait
