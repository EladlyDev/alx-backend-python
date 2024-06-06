#!/usr/bin/env python3
"""Module to work with typing"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list if it exists,
    otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
