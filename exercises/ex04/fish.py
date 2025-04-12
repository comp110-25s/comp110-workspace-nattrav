"""File to define Fish class."""


class Fish:
    """Defines the fish class."""

    age: int
    # fish only have an age

    def __init__(self):
        """Initializes the fish class."""
        self.age = 0
        return None

    # initializes fish to have an age of 0

    def one_day(self):
        """Defines one day in fish life."""
        self.age += 1
        return None

    # after one day, fish age increases by 1
