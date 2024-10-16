"""implement list utility functions"""

__author__ = 730739029


def only_evens(input1: list[int]) -> list[int]:
    """search through a list and only return the even numbers in a new list"""
    new_input: list[int] = []
    for x in input1:
        if x % 2 == 0:
            new_input.append(x)
    return new_input


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """return theelements of a list that fall between the start and stop ints"""
    new_list: list[int] = []
    index: int = start
    stop: int = end - 1
    if a_list == []:
        return []
    if index > stop:
        return []
    while index <= stop:
        new_list.append(a_list[index])
        index += 1
    return new_list
