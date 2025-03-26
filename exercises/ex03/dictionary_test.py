"""ex03 UNIT TESTS"""

author: str = "730578989"

import pytest

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert() -> None:
    # Tests the invert function, a use case
    assert invert({"og": "notog", "original": "new", "primary": "secondary"}) == {
        "notog": "og",
        "new": "original",
        "secondary": "primary",
    }


def test_invertedge() -> None:
    # Tests the invert function, an edge case, raises a KeyError
    with pytest.raises(KeyError):
        my_dictionary = {"og": "og", "new": "og", "primary": "secondary"}
        invert(my_dictionary)


def test_invert2() -> None:
    # Another use case for the invert function
    assert invert({"Blonde": "Jackie", "Brunette": "Sean", "Ginger": "Tabby"}) == {
        "Jackie": "Blonde",
        "Sean": "Brunette",
        "Tabby": "Ginger",
    }


def test_count() -> None:
    # A use case for the count function
    assert count(["Bananas", "Apples", "Oranges", "Bananas"]) == {
        "Bananas": 2,
        "Apples": 1,
        "Oranges": 1,
    }


def test_count2() -> None:
    # A second use case for the count function
    assert count(["Ping", "Pong", "Ping", "Pong"]) == {"Ping": 2, "Pong": 2}


def test_countedge() -> None:
    # An edge case for the count function
    assert count([]) == {}


def test_favorite_color() -> None:
    # A use case for the favorite_color function
    assert (
        favorite_color(
            {"Jeremy": "Orange", "Paul": "Orange", "Joel": "Pink", "Joan": "Orange"}
        )
        == "Orange"
    )


def test_favorite_color2() -> None:
    # A second use case for the favorite_color function
    assert (
        favorite_color({"Barry": "Blue", "Perry": "Pink", "Brian": "Brown"}) == "Pink"
    )


def test_favorite_coloredge() -> None:
    # An edge case for the favorite_color function that makes sure the first maximum counted color encountered is returned
    assert (
        favorite_color(
            {"Barry": "Blue", "Joey": "Red", "Eloise": "Blue", "Jackson": "Red"}
        )
        == "Blue"
    )


def test_ben_len() -> None:
    # A use case for the bin_len function
    assert bin_len(["Take", "a", "long", "break"]) == (
        {1: {"a"}, 4: {"Take", "long"}, 5: {"break"}}
    )


def test_ben_len2() -> None:
    # A second use case for the bin_len function
    assert bin_len(["Studying", "never", "stops"]) == (
        {5: {"never", "stops"}, 8: {"Studying"}}
    )


def test_bin_lenedge() -> None:
    # An edge test for the bin_len function
    assert bin_len(["", ""]) == ({0: {"", ""}})
