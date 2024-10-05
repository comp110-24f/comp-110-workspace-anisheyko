"""List utility functions"""

__author__ = 730739029


def all(a: list[int], b: int) -> bool:
    index: int = 0
    if len(a) == 0:
        return False
    while index < len(a):
        if a[index] != b:
            return False
        elif a[index] == b:
            index += 1
    return True  # return true can be at the same level of idnentation as the while statement bc if it iterated through each index and hasnt returned false, it must be true


def max(c: list[int]) -> int:
    index: int = 0
    biggest: int = c[index]
    # make local variabvle to keep track of current biggest num to compare the other nums to
    if len(c) == 0:
        raise ValueError("max() arg is an empty List")
    while index < len(c):
        if c[index] > biggest:
            biggest = c[index]
        index += 1
    return biggest


def is_equal(d: list[int], e: list[int]) -> bool:
    index: int = 0
    if len(d) != len(e):
        return False
    while index < len(e):
        if d[index] != e[index]:
            return False
        elif d[index] == e[index]:
            index += 1
    return True


def extend(f: list[int], g: list[int]) -> None:
    index: int = 0
    while index < len(g):  # do this since you can't append a list to another list
        f.append(
            g[index]
        )  # individually adds each element of list g to the edn of list f
        index += 1
