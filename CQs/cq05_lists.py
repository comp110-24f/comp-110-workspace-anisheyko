"""Mutating functions."""

__author__ = 730739029


def manual_append(param1: list[int], param2: int) -> None:
    param1.append(param2)


def double(param1: list[int]) -> None:
    index: int = 0
    while index < len(param1):
        param1[index] = 2 * param1[index]
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
