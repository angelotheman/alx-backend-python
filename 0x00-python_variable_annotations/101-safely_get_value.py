#!/usr/bin/env python3
"""
More annotations
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get the value
    """
    if key in dct:
        return dct[key]
    else:
        return default
