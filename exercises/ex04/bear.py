"""File to define Bear class."""


class Bear:
    """Creates bear class"""

    age: int
    hunger_score: int
    # bears have an age and a hunger score

    def __init__(self):
        """Initializes a bear object"""
        self.age = 0
        self.hunger_score = 0
        return None

    # bear start age and hunger at 0

    def one_day(self):
        """Represents one day of a bears life"""
        self.age += 1
        self.hunger_score -= 1
        return None

    # One day of a bear increases age by 1 and hunger score decreases by 1

    def eat(self, num_fish: int):
        """Defines how bears eat"""
        self.hunger_score += num_fish
        return None

    # bears hunger score increases with the number of fish
