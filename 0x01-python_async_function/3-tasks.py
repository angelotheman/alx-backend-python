#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from typing import Callable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Working to return the task
    """
    async def wrapper():
        """
        Wrapper function
        """
        return await wait_random(max_delay)
    return asyncio.create_task(wrapper())
