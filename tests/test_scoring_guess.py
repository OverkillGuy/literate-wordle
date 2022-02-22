"""Validates the Gherkin file features/scoring_guess.feature:

Feature: Scoring guesses
  As a Wordle game
  I need to tell the player how good their guess is
  In order to help them find the proper answer

Scenario: Perfect guess gives perfect score
  Given a wordle answer "crane"
  When scoring the guess "crane"
  Then score should be "🟩🟩🟩🟩🟩"
"""

import pytest

from literate_wordle.guess import score_guess


@pytest.mark.xfail(reason="Not implemented yet")
def test_perfect_guess():
    """Scenario: Perfect guess gives perfect score"""
    # Given a wordle answer "crane"
    answer = "crane"
    # When scoring the guess "crane"
    our_guess = "crane"
    score = score_guess(our_guess, answer)
    # Then score should be "🟩🟩🟩🟩🟩"
    assert score == "🟩🟩🟩🟩🟩", "Perfect answer should give Perfect Score"
