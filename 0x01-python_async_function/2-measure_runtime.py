#!/usr/bin/env python3
"""
Measuring the routine
"""
import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the routine
    """
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
