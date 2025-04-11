"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    # an int that tells you what day of the river's life cycle you are modeling
    bears: list[Bear]
    fish: list[Fish]
    # the lists represent the bear and fish populations

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        index: int = 0
        new_fish_list: list = []
        for item in self.fish:
            if item.age > 3:
                self.fish.pop(index)
            else:
                index += 1
        self.fish = new_fish_list
        index: int = 0
        new_bears_list: list = []
        for item in self.bears:
            if item.age > 5:
                self.bears.pop(index)
            else:
                index += 1
        self.bears = new_bears_list
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.fish.pop(3)
        return None

    def check_hunger(self):
        new_bear_list: list = self.bears
        index: int = 0
        for bear in new_bear_list:
            if bear.hunger_score < 0:
                new_bear_list.pop(index)
            else:
                index += 1
        self.bears = new_bear_list
        return None

    def repopulate_fish(self):
        n: int = len(self.fish)
        guppies: int = (n // 2) * 4
        x: int = 0
        while x <= guppies:
            self.fish.append(Fish())
            x += 1
        return None

    def repopulate_bears(self):
        n: int = len(self.bears)
        cubs: int = (n // 2) * 4
        x: int = 0
        while x <= cubs:
            self.bears.append(Bear())
            x += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        return None

    def remove_fish(self, amount: int):
        new_fish_list: list = self.fish
        index: int = 0
        while index < amount:
            new_fish_list.pop(index)
            index += 1
        self.fish = new_fish_list
        return None
