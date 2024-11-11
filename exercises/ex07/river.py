"""File to define River class."""

__author__ = "730739029"


from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Tracks the day of the week, and the fish and bear populations."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks ages of fish and bears, removes them if they're too old."""
        surviving_fish = []
        surviving_bears = []  # create new lists to asdd surviving animals to
        for fish in self.fish:  # calls Fish
            if fish.age <= 3:  # calls age attribute from Fish
                surviving_fish.append(fish)
        for bears in self.bears:
            if bears.age <= 5:
                surviving_bears.append(bears)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes amount number of fish."""
        for fish in range(0, amount):
            self.fish.pop(fish)
        return None

    def bears_eating(self) -> None:
        """Removes 3 fish that a bear ears if there are more than 5 fish."""
        for bears in self.bears:  # to access bears so you can access eat
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bears.eat(3)
        return None

    def check_hunger(self) -> None:
        """Creates new list for how many bears are fed by checing if their hunger is over 0."""
        fed_bears = []
        for bears in self.bears:
            if bears.hunger_score >= 0:  # bears.hunger_score accesses the bear file
                fed_bears.append(bears)
        self.bears = fed_bears
        return None

    def repopulate_fish(self) -> None:
        """Adds fish to the fish class based on their reproduction rate."""
        baby_fish = (len(self.fish) // 2) * 4
        for _ in range(
            0, baby_fish
        ):  # can use an underscore when you don't need to access that variable
            new_fish = (
                Fish()
            )  # assigns the new fish to the class so that they csn be added to the self.fish list
            self.fish.append(new_fish)
        return None

    def repopulate_bears(self) -> None:
        """Adds bears to the bear class based on their reproduction rate."""
        baby_bears = len(self.bears) // 2
        for _ in range(0, baby_bears):
            new_bears = Bear()
            self.bears.append(new_bears)
        return None

    def view_river(self) -> None:
        """Allows us to see the current fish and bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None

    def one_river_week(self) -> None:
        """Tracks the day."""
        for _ in range(
            7
        ):  # use underscore as place holder b/c wee don't need that variable
            self.one_river_day()
        return None
