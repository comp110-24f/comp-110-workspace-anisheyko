"""This file follows the Class Node through multiple linked list function calls."""

from __future__ import annotations

__author__: str = "730739029"


class Node:
    """Class that has two attributes, Value and Next, applied in later functions."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Creates self."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string."""
        rest: str = ""
        if self.next is None:
            rest = "None"
        else:
            rest = str(
                self.next
            )  # can also do self.next.__str__ bc __Str__ just represents objects as a string
        return f"{self.value}->{rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value}->{rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a linked list."""
    print(head.value)
    if head.next is None:
        return head.value  # this is called a base case
    else:
        return last(
            head.next
        )  # if its not the last one, you ask the NEXT node, this is the recursive case


print(last(one))  # expect 2
print(last(courses))  # expect 301


def value_at(head: Node | None, index: int) -> int:
    """Locate the value that corresponds to the given index."""
    if head is None:  # first base case
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # second base case
        return head.value
    else:  # recursive case
        return value_at(
            head.next, index - 1
        )  # starts a5t the end and moves one index to the left until the right index is found
    # index -1 and head.next modifies both arguments, and moves you closer to base case by subtracting


def max(head: Node | None) -> int:
    """Find and return the max/biggest5 number in the node."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    rest: int = max(head.next)
    if head.value > rest:
        return head.value
    else:
        return rest


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)."""
    if start == end:
        return None
    else:
        return Node(start, recursive_range(start + 1, end))


def linkify(items: list[int]) -> Node | None:
    """Return a linked list of nodes the same as the input list."""
    if len(items) == 0:
        return None
    else:
        return Node(
            items[0], linkify(items[1:])
        )  # value is assigned the first item in the list, next is assigned a function call to the nect item in the list


def scale(head: Node | None, factor: int) -> Node | None:
    """Scales every item in a list by a factor."""
    if head is None:
        return None
    else:
        return Node(
            (head.value) * factor, scale(head.next, factor)
        )  # don't need to modify first parameter of second call because when it's call the first parameter of the fist call will modify it


# print(scale(linkify([1, 2, 3]), 2))
