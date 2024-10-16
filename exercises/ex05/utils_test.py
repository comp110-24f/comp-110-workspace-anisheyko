"""define test functions for our utils"""

__author__ = 730739029

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edge_case() -> None:
    """tests to make sure only evens works properly with an edge case"""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_return() -> None:
    """tests to make sure only evens returns the expected list"""
    numbers: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(numbers) == [2, 4]


def test_only_evens_mutate() -> None:
    """tests to make sure only evens doesnt mutate the original list"""
    numbers: list[int] = [1, 2, 3, 4, 5]
    only_evens(numbers)  # call function without asserting first
    assert numbers == [1, 2, 3, 4, 5]

    # assert that input1 as numbers still returns the full list


def test_sub_edge_case() -> None:
    """tests to make sure sub returns an empty list when provided an empty list"""
    numbers: list[int] = []
    assert sub(numbers, 1, 3) == []


def test_sub_return() -> None:
    """tests to make sure that sub returns only even numers in the list"""
    numbers: list[int] = [1, 2, 3, 4, 5]
    assert sub(numbers, 1, 3) == [2, 3]


def test_sub_mutate() -> None:
    """tests to make sure a_list is not mutated when sub is called"""
    numbers: list[int] = [1, 2, 3, 4, 5]
    sub(numbers, 1, 3)
    assert numbers == [1, 2, 3, 4, 5]


import pytest


def test_add_at_index_edge_case() -> None:
    """tests to make sure IndexError is returned at edge cases"""
    numbers: list[int] = [1, 2, 3, 4, 5]
    with pytest.raises(IndexError):
        add_at_index(numbers, 3, -2)


def test_add_at_index_return() -> None:
    """tests to make sure None is returned, since the function has the return type None"""
    numbers: list[int] = [6, 7, 9, 10]
    assert (
        add_at_index(numbers, 8, 2) == None
    )  # none not the list b/c the return typer is none


def test_add_at_index_mutate() -> None:
    """tests to make sure the original list_1 IS mutated"""
    numbers: list[int] = [6, 7, 9, 10]
    add_at_index(numbers, 8, 2)
    assert numbers == [6, 7, 8, 9, 10]
