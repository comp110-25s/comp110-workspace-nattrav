"""Creating Wordle"""

__author__: str = "730578989"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        print(f"=== turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 7
        if turn == 6:
            print("X/6 - Sorry, try again tomorrow")
        turn = turn + 1


# the main function tells the player what turn they are on and if they won or lost by calling the other functions


def contains_char(guess: str, character: str) -> bool:
    """Does the guess contain the character?"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(guess):
        if guess[idx] == character:
            return True
        else:
            idx = idx + 1

    return False


# this function determines if the guess contains the character by using a while loop that repeats through each index of the guess and returns True if it does contain the character and false if not


def emojified(guess: str, secret: str) -> str:
    """Codifies results of a guess into emojis"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    results: str = ""
    idx: int = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            results = results + GREEN_BOX
            idx = idx + 1
        elif contains_char(secret, guess[idx]):
            results = results + YELLOW_BOX
            idx = idx + 1
        else:
            results = results + WHITE_BOX
            idx = idx + 1

    return results


# this function codifies the results of the guess into different color boxes by calling the contains_char function and if the guess does contain that character at that index it will be green, if it does contain it at a different index it will be yellow, and if not it will be white


def input_guess(expected_len: int) -> str:
    """Tells player to enter a certain character word or to try again"""
    N: int = expected_len
    input_guess: str = input(f"Enter a {N} character word:")
    while len(input_guess) != N:
        input_guess = input(f"That wasn't {N} chars! Try again:")
    return input_guess


# this function determines the expected length and if the guess is the correct length

if __name__ == "__main__":
    main(secret="codes")
