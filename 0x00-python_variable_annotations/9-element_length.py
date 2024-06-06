#!/usr/bin/env python3
"""Module to work with typing"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples where each tuple contains
    a sequence and its length"""
    return [(i, len(i)) for i in lst]
