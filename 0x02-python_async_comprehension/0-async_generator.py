#!/usr/bin/env python3

"""
asynchronous `async_generator` coroutine
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    yields any value between  0 and 10
    asynchronously waits 1 sec between each yield
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
