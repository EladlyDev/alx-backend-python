#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time"""
    p = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - p)
