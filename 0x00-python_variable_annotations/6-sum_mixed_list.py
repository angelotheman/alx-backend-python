#!/usr/bin/env python3
"""
Type annotated function
"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    Returns sum
    """
    return sum(mxd_lst)
