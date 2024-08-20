#!/usr/bin/env python3
"""Simple Pagination Function"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing start index and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
