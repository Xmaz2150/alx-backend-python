#!/usr/bin/env python3

"""
asynchronous `async_comprehension` coroutine
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    returns list of floats assigned from an
    asynchronous comprehension
    """
    return [n async for n in async_generator()]
