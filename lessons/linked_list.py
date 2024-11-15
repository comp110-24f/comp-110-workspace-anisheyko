from __future__ import annotations

__author__: str = "730739029"


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
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


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)"""
    if start > end:  # raising an exception for an edge case error
        raise ValueError("Invalid use of recursive_range")
    if start == end:
        return None
    else:  # recurive case intuition:handle the first case based on the specific call then build the rest of the list using the builder function recursively
        return Node(start, recursive_range(start + 1, end))


# or you can rewrite like this
def recursive_range_2(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)"""
    if start == end:
        return None
    else:  # recurive case intuition:handle the first case based on the specific call then build the rest of the list using the builder function recursively
        first: int = start
        rest: Node | None = recursive_range_2(start + 1, end)
        return Node(first, rest)


a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)
print(a)
print(b)
