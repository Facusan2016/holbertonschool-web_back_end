#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in
parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import time
from asyncio import Task, gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function to measure the time"""
    start = time.monotonic()
    tasks = [Task(async_comprehension()) for i in range(4)]
    await gather(*tasks)

    return (time.monotonic() - start)
