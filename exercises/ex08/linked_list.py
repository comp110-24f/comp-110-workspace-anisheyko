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


def value_at(head: Node | None, index: int) -> int:
    if head is None:  # first base case
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # second base base
        return head.value
    else:  # recursive case
        return value_at(
            head.next, index - 1
        )  # starts a5t the end and moves one index to the left until the right index is found
    # index -1 and head.next modifies both arguments, and moves you closer to base casse by subtracting


def max(head: Node | None) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    rest: int = max(head.next)
    if head.value > rest:
        return head.value
    else:
        return rest
