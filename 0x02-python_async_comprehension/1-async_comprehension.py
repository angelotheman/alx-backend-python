#!/usr/bin/env python3
"""
List comprehension
"""
import asyncio
from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    return [number async for number in async_generator()]
