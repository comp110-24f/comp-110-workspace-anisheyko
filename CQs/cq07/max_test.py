__author__ = 730739029

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_return_max() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(numbers) == 5


def test_find_and_return_max1() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]
    find_and_remove_max(numbers)
    assert numbers == [1, 2, 3, 4]


def test_find_and_return_max2() -> None:
    numbers: list[int] = []
    assert find_and_remove_max(numbers) == -1
