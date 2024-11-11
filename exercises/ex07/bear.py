"""File to define Bear class."""

__author__ = "730739029"


class Bear:
    """Bear population by river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initiates the ages of the bears in the population."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Increases the age of the bear in the population every day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Monitors the hunger_score based on ho3 many fish the bears have eaten."""
        self.hunger_score += num_fish
        return None
