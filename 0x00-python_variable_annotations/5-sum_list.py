#!/usr/bin/env python3
from typing import Iterable


def sum_list(input_list: Iterable[float]) -> float:
    """ takes a list of floats and returns there sum """
    sum: float = 0.0
    for x in input_list:
        sum += x
    return sum
