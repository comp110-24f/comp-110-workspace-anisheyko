"""using a while loop to iterate over a string"""

__author__ = "730739029"


def num_instances(phrase: str, search_char: str) -> int:
    """this function identifies a phrase and a specific character to be used"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if (phrase[index]) == search_char:
            # index goes in brackets because brackets are how you identify a
            # specific letter in a specific position
            count = count + 1
            index = index + 1
        else:
            index = index + 1
        # make sure to create else function to ensure that the loop keeps going even
        # if the character doesn't appear in the word
    print(count)
    return count


num_instances(phrase="Happy Tuesday!", search_char="y")
