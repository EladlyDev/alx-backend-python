#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""
from functools import reduce
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    ''' returns sum of all values of list '''
    return reduce(lambda a, b: a + b, input_list)
