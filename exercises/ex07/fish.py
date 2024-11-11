"""File to define Fish class."""

__author__ = "730739029"


class Fish:
    """Fish population in river."""

    age: int

    def __init__(self):
        """Initiates the ages of the fish in the population."""
        self.age = 0

    def one_day(self) -> None:
        """Increases the age of the fish in the population every day."""
        self.age += 1
        return None
