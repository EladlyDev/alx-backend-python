#!/usr/bin/env python3
""" Concurrent coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """"runs wait_random n times"""
    out: List[float] = [wait_random(max_delay) for a in range(n)]
    return [
        await val
        for val in asyncio.as_completed(out)
    ]
