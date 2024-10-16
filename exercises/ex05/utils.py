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
    """return the elements of a list that fall between the start and stop ints"""
    new_list: list[int] = []
    index: int = start
    stop: int = end - 1
    if a_list == []:
        return []
    if index > stop:
        return []
    if start < 0:
        index = 0
    if end > len(a_list) - 1:
        stop = len(a_list) - 1
        # you change the value of stop not end because stop is the local variable created inside the body
    if end <= 0:
        return []
    # cant use elif statmeents because multiple might be true
    while index <= stop:
        new_list.append(a_list[index])
        index += 1
    return new_list


def add_at_index(list_1: list[int], add_this: int, add_to: int) -> None:
    """adds an int to a list at a specific index"""
    if add_to < 0:
        raise IndexError("Index is out of bounds for the input list")
    if add_to > len(list_1):
        raise IndexError("Index is out of bounds for the input list")
    list_1.append(
        0
    )  # adds 0 to the end of the list so it can be replaced with add_this
    x = len(list_1) - 1  # so it starts at the last index of the list
    while x > add_to:
        list_1[x] = list_1[x - 1]
        x -= 1  # moves one index to the left, until it finds add_to
    list_1[add_to] = add_this
