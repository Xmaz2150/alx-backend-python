#!/usr/bin/env python3

"""
element_length annotated module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    adding annotations:
        lst as iterable input
        returns list of tuples
    """
    return [(i, len(i)) for i in lst]
