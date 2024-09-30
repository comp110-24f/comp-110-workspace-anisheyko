"""Wordle, six guesses to guess a word"""

__author__ = "730739029"


def input_guess(secret_word_len: int) -> str:
    """allows you to guess a word that must match the guess"""
    guess: str = input("Enter a " + str(secret_word_len) + " character word:")
    if len(guess) == secret_word_len:
        print(guess)
        exit()
    else:
        while len(guess) != secret_word_len:
            print("That wasn't" + str(secret_word_len) + "! Try again:")
            input_guess(secret_word_len=secret_word_len)
            # need to call input_guess again or esle itll be an infinite loop
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """char will search through search_word for a matching char"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            print("True")
            exit()
        elif secret_word[index] != char_guess:
            index += 1
    if index == len(secret_word):
        print("False")
