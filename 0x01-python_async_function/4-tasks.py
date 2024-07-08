#!/usr/bin/env python3

"""
asynchronous `task_wait_n` coroutine
module
"""
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    return time waited for calling `wait_random` n times
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return sorted(await asyncio.gather(*tasks))
