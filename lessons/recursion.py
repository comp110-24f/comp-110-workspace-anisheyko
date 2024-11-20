"""Recursive functions without recursive structures"""


def factorial(n: int) -> int:
    """Returns the factorial of n using recursive structures."""
    if n < 0:
        raise ValueError("cannot call factorial on a negative number!")  # edge case
    if n == 0 or n == 1:  # base case
        return 1
    else:
        return n * factorial(
            n - 1
        )  # multiplies n by the result of calling facotrial on n-1, until base case is reached
