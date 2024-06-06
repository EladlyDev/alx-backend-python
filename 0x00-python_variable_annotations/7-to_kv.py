#!/usr/bin/env python3
"""Type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple containing the str and the square of the v"""
    return (k, v**2)
