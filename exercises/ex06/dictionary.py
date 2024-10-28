"""Practice with Dictionary functions"""

__author__ = 730739029


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """this function will switch the keys and values in each pair"""
    duplicates: list[str] = []  # will sotre the values in dict_1
    for key in dict_1:
        if (
            dict_1[key] in duplicates
        ):  # checks to see if the value at the indexs already exists in duplicates
            raise KeyError(
                "This value exists multiple times, we cant reverse it!"
            )  # rasie works like a return statement, so it wont reverse it if this error is called
        duplicates.append(dict_1[key])

    reverse_dict: dict[str, str] = {}
    for key in dict_1:
        value = dict_1[key]  # this finds what the value is at that key
        reverse_dict[value] = (
            key  # this sets the value of the og dict as the key of the new list
        )
    return reverse_dict


def favorite_color(name_color: dict[str, str]) -> str:
    color_count: dict[str, int] = {}
    dict_1: dict[int, str] = {}
    dict_2: dict[str, int] = {}

    for (
        key
    ) in (
        name_color
    ):  # runs through this whole for loop firs,t making a dict of the frerqwuency a color shows up
        color: str = name_color[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_value: int = 0
    for key in color_count:
        if color_count[key] > max_value:
            max_value = color_count[key]
        dict_2[key] = (
            max_value  # identifies which color had the biggest frequency in that dict
        )
    for key in dict_2:
        dict_1[(color_count[key])] = key  # flips

    return dict_1[max_value]


def count(name: list[str]) -> dict[str, int]:
    frequency: dict[str, int] = {}

    for elem in name:
        if elem in frequency:
            frequency[elem] += 1
        else:
            frequency[elem] = 1
    return frequency


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    frequency: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if (
            first_letter not in frequency
        ):  # if that key doesn't exist yet, create am empty lift for that letter, need to initialize an empty list since its as list at the value not just a str
            frequency[first_letter] = []
        frequency[first_letter].append(
            word
        )  # add the value to the key at the correct first letter. not at same indent as the empty list b/c then it wouldnt add anything if it that key does already exist
    return frequency


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:

    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]
    return None
