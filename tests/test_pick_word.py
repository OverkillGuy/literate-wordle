"""Validates the Gherkin file features/pick_answer_word.feature:

Feature: Pick an answer word
  As a Wordle game
  I need to pick a random 5 letter word
  In order to let players guess it
"""

from literate_wordle.words import pick_answer_word


def test_pick_word_ok_length():
    """Confirm a wordle solution is of right size"""
    assert len(pick_answer_word()) == 5, "Picked wordle solution is wrong size!"
