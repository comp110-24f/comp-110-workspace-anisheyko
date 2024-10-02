"""Wordle, six guesses to guess a word"""

__author__ = "730739029"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_num: int = 0
    max_turn_num: int = 6
    won: bool = False
    while turn_num < max_turn_num and not won:
        print(
            f"===turn {turn_num+1}/6==="
        )  # turn_num+=1 bc we havent added 1 to turn yet so it shwos up as 0
        user_guessed_this: str = input_guess(secret_word_len=len(secret))
        each_round_output: str = emojified(guess=user_guessed_this, secret=secret)
        print(each_round_output)
        turn_num += 1
        if user_guessed_this == secret:
            won = True
    if max_turn_num == 6 and not won:
        print("X/6 - Sorry, try again tomorrow!")
    elif won == True:
        print(f"you won in {turn_num}/6 turns!")


def input_guess(secret_word_len: int) -> str:
    """allows you to guess a word that must match the guess"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    if len(guess) == secret_word_len:
        return guess
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
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
        index += 1
    return False


# dont need an else statement to return false, just put it on the same indentation as while bc if thew while is dont itll just go to the return statement


def emojified(guess: str, secret: str) -> str:
    """return colored emojis to indicate whether a character in the guess is in the correct/incorrect position"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    final_print: str = ""
    # use a global variable to keep track of all the outputs and itll combine them into one str instead of printing them each in sep lines
    index: int = 0
    while index < len(
        guess
    ):  # use index not len=len and itll circle through both indexes
        while index < len(secret):
            if guess[index] == secret[index]:
                final_print += GREEN_BOX
                index += 1
            elif contains_char(secret_word=secret, char_guess=guess[index]) == True:
                final_print += YELLOW_BOX
                index += 1
            else:
                final_print += WHITE_BOX
                index += 1
    return final_print
    # return statement must go under the outsdie while loop


if __name__ == "__main__":
    main(secret="codes")
