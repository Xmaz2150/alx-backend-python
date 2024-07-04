#!/usr/bin/env python3

"""
to_kv annotated module
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    teturns string k and the square of v as a float all as tuple[str, float]
    """
    return (k, float(v ** 2))
