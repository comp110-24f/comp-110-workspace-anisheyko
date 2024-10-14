__author__ = 730739029


def find_and_remove_max(input1: list[int]) -> int:
    index: int = 0
    max: int = 0  # had to make it 0 not input1[index] or erlse id get an error
    if input1 == []:
        return -1
    for x in input1:
        if x > max:
            max = x
    while index < len(input1):
        if input1[index] == max:
            input1.pop(index)
        index += 1
    # print(input1)
    return max
