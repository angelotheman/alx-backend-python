#!/usr/bin/env python3
"""
Iterable objects
"""
from typing import Tuple, Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return annonated version of element_length
    """
    return [(i, len(i)) for i in lst]
