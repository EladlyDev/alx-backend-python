#!/usr/bin/env python3
""" Basic async syntax """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random number and returns it"""
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return (rand)
