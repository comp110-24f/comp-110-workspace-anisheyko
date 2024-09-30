"""basic syntax with lists"""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal
# either works

my_numbers.append(1.5)

game_points: list[int] = [102, 86, 94, 102]

print(game_points[3])

game_points[1] = 72
# print(len(game_points))

game_points.pop(1)
# print(game_points)


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(input=game_points)
