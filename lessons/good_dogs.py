def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> Bool:
    num_dogs: int = len(scores)
    if num_dogs <= idx:  # edge case, the index is not inside the list
        raise IndexError("idx too high")
    elif (
        int(scores[idx]["score"]) < thresh
    ):  # base case, eaisesrt way to get a return statement is for something to return False, bc it only needs to happen once
        return False
    else:
        if (
            num_dogs == idx + 1
        ):  # returns true if its gotten to the end of the list, bc it wouldn't have gotten there if it reached a false return statement
            return True
        else:
            return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]
