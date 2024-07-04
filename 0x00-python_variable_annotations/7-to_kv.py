#!/usr/bin/env python3

"""
sum_mixed_list annotated module
"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    teturns string k and the square of v as a float all as tuple[str, float]
    """
    return (k, float(v ** 2))
