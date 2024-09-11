"""planning the number of guests, teabags, treats, and the total cost of tea party"""

__author__: str = "730739029"


def main_planner(guests: int) -> None:
    "this is the main function what will call all the other functions in the code"
    print("A Cozy tea Party for" + str(guests) + "People!")
    print("Tea Bags:" + str(tea_bags(people=guests)))
    print("Treats:" + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=guests, treat_count=guests)))
    return None


# had to manually put str in from of each print function to convert the integers to
# str or else I would get error messages


def tea_bags(people: int) -> int:
    """number of tea bags for the people attending the tea party"""
    return 2 * people


def treats(people: int) -> int:
    """number of treats for the people attending the tea party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """:cost of the tea bags and treats combined"""
    return (treats(people=treat_count) * 0.75) + (tea_bags(people=tea_count) * 0.50)


# had to undue the multiplication done to tea_bags and treats by dividing both
# functions by 3 and 2 respectively
