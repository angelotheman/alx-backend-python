#!/usr/bin/env python3
"""
Type annotated function
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    Returns sum
    """
    return sum(mxd_lst)
