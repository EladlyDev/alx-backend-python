#!/usr/bin/env python3
"""measure runtime"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the runtime"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return asyncio.get_event_loop().time() - start
