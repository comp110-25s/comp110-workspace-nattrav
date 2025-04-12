"""File to define River class."""

__author__: str = "730578989"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Defines the river class with bears and fish."""

    day: int
    # an int that tells you what day of the river's life cycle you are modeling
    bears: list[Bear]
    fish: list[Fish]
    # the lists represent the bear and fish populations

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages and kills them if they are over a certain age."""
        index: int = 0
        for item in self.fish:
            if item.age > 3:
                self.fish.pop(index)
            else:
                index += 1
        # for every fish in the list it pops them off if the age is over 3
        index: int = 0
        for item in self.bears:
            if item.age > 5:
                self.bears.pop(index)
            else:
                index += 1
        # for every bear in the list it pops them off if the age is over 5
        return None

    def bears_eating(self):
        """The bears eat 3 fish if there are at least 5 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        # goes through each index (bear) in the bear list and if there are more than 5 fish, the bear eats 3 and it removes it from the list
        return None

    def check_hunger(self):
        """Kills the bears if they starve."""
        new_bear_list: list = self.bears
        index: int = 0
        for bear in new_bear_list:
            if bear.hunger_score < 0:
                new_bear_list.pop(index)
            else:
                index += 1
        self.bears = new_bear_list
        # Goes through each index in the bear list and pops off any starved bears
        return None

    def repopulate_fish(self):
        """If there are two fish, they will have 4 guppies."""
        n: int = len(self.fish)
        guppies: int = (n // 2) * 4
        while guppies >= 1:
            self.fish.append(Fish())
            guppies -= 1
        # If there are two fish, they will have 4 babies and the base case keeps it from having infinite recursion
        return None

    def repopulate_bears(self):
        """If there are two bears, they will have 1 cub."""
        n: int = len(self.bears)
        cubs: int = n // 2
        while cubs >= 1:
            self.bears.append(Bear())
            cubs -= 1
        # If there are two bears they will have one cub that will be appended to the list and the base case is cubs -= 1 to prevent infinite recursion
        return None

    def view_river(self):
        """Tells you the day and populations."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        # uses f strings to print out the length of the lists of bears and fish as the population
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Gives 7 days to make a week."""
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        # calls the one_river_day function seven times to represent a week
        return None

    def remove_fish(self, amount: int):
        """Removes fish from the list."""
        new_fish_list: list = self.fish
        index: int = 0
        while index < amount:
            new_fish_list.pop(index)
            index += 1
        self.fish = new_fish_list
        # removes fish from the list by going through each index. uses a separate list to prevent self.fish from going back each index
        return None
