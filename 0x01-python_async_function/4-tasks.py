#!/usr/bin/env python3
"""
Task 4 module
"""
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """
    Wait random helper function
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Main function
    """
    return asyncio.create_task(wait_random(max_delay))
