#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def f(fl: float) -> float: return fl*multiplier
    return f
