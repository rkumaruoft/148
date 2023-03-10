"""CSC148 Lab 1

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from search import binary_search


def test_search() -> None:
    """Simple test for binary_search."""
    assert binary_search([2, 4, 7, 8, 11], 11) == 4


def test_single_item_list() -> None:
    """Test binary search with single item."""
    assert binary_search([11], 11) == 0


if __name__ == '__main__':
    import pytest

    pytest.main(['test_search.py'])
