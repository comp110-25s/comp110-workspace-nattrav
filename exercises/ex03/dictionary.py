"""EX03 Dictionary Functions Code"""

__author__: str = "730578989"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary"""
    inverted_dict: dict[str, str] = {}
    list_to_count: list = []
    for key in dictionary:
        if dictionary[key] in list_to_count:
            raise KeyError("Dictionary contains duplicate values")
        # raises a KeyError if the value at that key is already in list_to_count because that means it's a repeat since it hasn't appended anything yet
        list_to_count.append(dictionary[key])
    for key in dictionary:
        value: str = dictionary[key]
        inverted_dict[value] = key
        # goes through each value in dictionary, assigns it to a variable named value, then makes that value the key in a new dictionary inverted_dict and the old key the new value
    return inverted_dict


def count(list: list[str]) -> dict[str, int]:
    """Makes each list item into a key and makes the count of the item into the value"""
    countdict: dict[str, int] = {}
    for item in list:
        if item in countdict:
            countdict[item] += 1
        else:
            countdict[item] = 1
    return countdict


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Returns the most frequent favorite color"""
    colors_list: list = []
    for key in fav_colors:
        colors_list.append(fav_colors[key])
        # This part adds every value in fav_colors to a list so it can be put into the count function
    countdict: dict[str, int] = count(colors_list)
    max: int = 0
    color: str = ""
    for key in countdict:
        if countdict[key] > max:
            max = countdict[key]
            color = key
    return color


def bin_len(to_bin: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into a dictionary where the key is the length of the item and it's values are a set of strings from the item"""
    binned: dict[int, set[str]] = {}
    for index in to_bin:
        characters: int = len(index)
        if characters in binned:
            binned[characters].add(index)
        else:
            settemp: set[str] = set()
            binned[characters] = settemp
            binned[characters].add(index)
    return binned
