"""Practice with conditionals, local variables, and user input"""

__author__ = 730739029


def guess_a_number() -> None:
    secret: int = 7
    response = int(input("Guess a number:"))
    # response can techinaclly be any word, it is just functioning as a local variable holder
    print("Your guess was " + str(response))
    if response == 7:
        print("You got it!")
    elif response < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif response > secret:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
# guess_a_number()
