"""Dummy package"""
from typing import List


def to_string(users: List[str]) -> str:
    """Joins list values to a single string value"""
    return ', '.join(users)
