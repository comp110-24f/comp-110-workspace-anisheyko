"""practice with unit tests"""


def get_first(a: list[str]) -> str:
    """return first element."""
    return a[0]


def remove_first(b: list[str]) -> None:
    """remove first element."""
    b.pop(0)
    return None


def get_and_remove_first(c: list[str]) -> str:
    """remove AND return first element"""
    first: str = c[0]
    c.pop(0)
    return first
