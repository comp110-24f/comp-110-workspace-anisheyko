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


invert({"kris": "jordan", "michael": "jordan"})
