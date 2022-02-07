"""Basic tests of literate_wordle."""

from literate_wordle.wordle import add_two_ints


def test_two_integers_work():
    """Confirm silly function works"""
    assert add_two_ints(7,3) == 7 + 3, "Bad addition function"
