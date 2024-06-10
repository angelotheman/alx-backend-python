#!/usr/bin/env python3
"""
Annotated Callables
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Main function
    """
    def multiplier_function(x: float) -> float:
        """
        Callable function
        """
        return x * multiplier
    return multiplier_function
