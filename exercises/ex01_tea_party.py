"""A program to plan a tea party"""

__author__: str = "730578989"


def main_planner(guests: int) -> None:
    """Calls each function and produces printed output"""
    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)) + "")
    print("Treats: " + str(treats(people=guests)) + "")


def tea_bags(people: int) -> int:
    """Computes the number of tea bags per guest"""
    return people * 2


def treats(people: int) -> int:
    """Computes the number of treats per guest"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of tea and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
