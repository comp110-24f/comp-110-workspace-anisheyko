"""Wordle, six guesses to guess a word"""

__author__ = "730739029"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_num: int = 1
    while turn_num <= 6:
        print("===turn" + str(turn_num) + "/6===")
        input_guess(secret_word_len=len(secret))
        print(emojified(guess=, secret=secret))


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
            index = index
            return True
        elif secret_word[index] != char_guess:
            index += 1
    if index == len(secret_word):
        return False


def emojified(guess: str, secret: str) -> str:
    """return colored emojis to indicate whether a character in the guess is in the correct/incorrect position"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    while len(guess) <= len(secret):
        if guess[index] == secret[index]:
            print(GREEN_BOX)
            index += 1
        elif contains_char(secret_word=secret, char_guess=guess[index]) == True:
            print(YELLOW_BOX)
            index += 1
        else:
            print(WHITE_BOX)
            index += 1
