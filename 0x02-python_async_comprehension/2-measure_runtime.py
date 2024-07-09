#!/usr/bin/env python3

"""
asynchronous `measure_runtime` coroutine
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    returns the elapsed time after running tasks
    in parallel?
    """
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    start_time = time.time()

    await asyncio.gather(*tasks)

    end_time = time.time()

    return end_time - start_time

if __name__ == "__main__":
    asyncio.run(measure_time())
