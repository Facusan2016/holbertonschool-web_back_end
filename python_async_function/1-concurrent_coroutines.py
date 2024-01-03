#!/usr/bin/env python3
"""
import wait_random from the previous python
file that you’ve written and write an async
routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async function to return coro wait_random values n times"""
    background_tasks = []

    for _ in range(n):
        background_tasks.append(
            asyncio.create_task(wait_random(max_delay))
        )

    task_res = []

    for task in asyncio.as_completed(background_tasks):
        task_res.append(await task)

    return task_res
