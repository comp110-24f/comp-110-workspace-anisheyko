"""Wordle, six guesses to guess a word"""

__author__ = "730739029"


def input_guess(secret_word_len: int) -> str:
    guess: str = input("Enter a " + str(secret_word_len) + " character word:")
    if len(guess) == secret_word_len:
        print(guess)
    else:
        while len(guess) != secret_word_len:
            print("That wasn't 5 chars! Try again:")
    return guess
