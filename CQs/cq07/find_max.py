__author__ = 730739029


def find_and_remove_max(input1: list[int]) -> int:
    index: int = 0
    max: int = input1[0]
    if len(input1) == []:
        return -1
    while index < len(input1):
        if input1[index] > max:
            max = input1[index]
        index += 1
    while index < len(input1):
        index = input1[0]
        if input1[index] == max:
            input1.pop(index)
        index += 1
    return max
