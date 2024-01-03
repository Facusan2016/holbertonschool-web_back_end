#!/usr/bin/env python3
"""
Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Async function to return coro wait_random values n times"""
    background_tasks = []

    for _ in range(n):
        background_tasks.append(
            task_wait_random(max_delay)
        )

    task_res = []

    for task in asyncio.as_completed(background_tasks):
        task_res.append(await task)

    return task_res
