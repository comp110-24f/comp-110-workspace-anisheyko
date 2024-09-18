"""EX02- Chardle: A cute step toward Wordle."""

__author__ = "730739029"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# once main function is called with contains_char inside of it,
# delete the function call that was at the end of all the code

# this is a call not a def of contains_char, so you write
# the function w the arguements not parameters


def input_word() -> str:
    """allows you to input a five letter word"""
    choose_word: str = input("Enter a 5-character word: ")
    if len(choose_word) == 5:
        print("'" + choose_word + "'")
        # had to make sure to put ' or else they wouldnt appear around the printed word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        print("'" + choose_word + "'")

        # put exit after the error meassage under ther same indentation
    return choose_word


def input_letter() -> str:
    """allows you to input a single character"""
    choose_letter: str = input("Enter a single character: ")
    if len(choose_letter) == 1:
        print("'" + choose_letter + "'")
    else:
        print("Error: Character must be a single character")
        exit()
        print("'" + choose_letter + "'")

    return choose_letter

    # def contains_char(word: str, letter: str) -> None:
    # """finds there character mathced within the word"""
    # print("Searching for " + letter + " in " + word)
    # dont forget the spaces after the words before ending the quotation
    # match_count: int = 0
    # if word[0] == letter:
    # match_count = match_count + 1
    # you do match_count=match_count and not int bc int is just there to
    # say match_count has to be an int
    # print(letter + " found at index 0")
    # if word[1] == letter:
    # match_count = match_count + 1
    # print(letter + " found at index 1")
    # if word[2] == letter:
    # match_count = match_count + 1
    # print(letter + " found at index 2")
    # if word[3] == letter:
    # match_count = match_count + 1
    # print(letter + " found at index 3")
    # if word[4] == letter:
    # match_count = match_count + 1
    # print(letter + " found at index 4")


# if match_count > 0:
# print(str(match_count) + " instances of " + letter + " found in " + word)
# else:
# print("No instances of " + letter + " found in " + word)


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    match_count: int = 0
    index: int = 0
    while index < len(word):
        if (word[index]) == letter:
            match_count += 1
            index += 1
            print(str(match_count) + " instances of " + letter + " found in " + word)
        elif (word[index]) != input_letter:
            index += 1
        else:
            print("No instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
