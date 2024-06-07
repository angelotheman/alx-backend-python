#!/usr/bin/env python3
"""
Type annotated function
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Returns sum
    """
    return sum(mxd_lst)
