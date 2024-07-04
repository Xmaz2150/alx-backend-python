#!/usr/bin/env python3

"""
make_multiplier annotated module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns function that takes a float and returns its
    product with multiplier as Callable[[float], float]
    """
    def multiplier_f(x: float) -> float:
        return x * multiplier

    return multiplier_f
