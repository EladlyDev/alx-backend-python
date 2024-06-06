#!/usr/bin/env python3
from typing import Iterable, Union


def sum_mixed_list(mxd_lst: Iterable[Union[float, int]]) -> float:
    """Takse a mixed list of ints and floats and returns the sum as a float"""
    sum: float = 0.0
    for x in mxd_lst:
        sum += x
    return sum
