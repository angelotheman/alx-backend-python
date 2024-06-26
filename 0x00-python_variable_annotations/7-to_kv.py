#!/usr/bin/env python3
"""
Complex types string int and float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    From to_kv
    """
    return (k, v ** 2)
