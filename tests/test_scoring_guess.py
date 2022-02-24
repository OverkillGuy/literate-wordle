"""Validates the Gherkin file features/scoring_guess.feature:

Feature: Scoring guesses
  As a Wordle game
  I need to tell the player how good their guess is
  In order to help them find the proper answer

Scenario: Perfect guess gives perfect score
  Given a wordle answer "crane"
  When scoring the guess "crane"
  Then score should be "🟩🟩🟩🟩🟩"

Scenario: No character in common
  Given a wordle answer "brave"
  When scoring the guess "skill"
  Then score should be "⬜⬜⬜⬜⬜"

Scenario: Character in wrong place
  Given a wordle answer "rebus"
  When scoring the guess "skull"
  Then score should be "🟨⬜🟨⬜⬜"

Scenario Outline: Scoring guesses
  Given a wordle <answer>
  When scoring <guess>
  Then score should be <score>

# Emoji (Unicode) character rendering is hard:
# Please forgive the table column alignment issues!
  Examples: A few guesses and their score
    | answer  | guess	| score		|
    | adage   | adobe	| 🟩🟩⬜⬜🟩	|
    | serif   | quiet	| ⬜⬜🟨🟨⬜	|
    | raise   | radix	| 🟩🟩⬜🟨⬜	|
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


@pytest.mark.xfail(reason="Not implemented yet")
def test_no_common_character():
    """Scenario: No character in common"""
    # Given a wordle answer "brave"
    answer = "brave"
    # When scoring the guess "skill"
    our_guess = "skill"
    score = score_guess(our_guess, answer)
    # Then score should be "⬜⬜⬜⬜⬜"
    assert score == "⬜⬜⬜⬜⬜", "No character in common with answer should give 0 score"


@pytest.mark.xfail(reason="Not implemented yet")
def test_wrong_place():
    """Scenario: Character in wrong place"""
    # Given a wordle answer "rebus"
    answer = "rebus"
    # When scoring the guess "skull"
    our_guess = "skull"
    score = score_guess(our_guess, answer)
    # Then score should be "🟨⬜🟨⬜⬜"
    assert score == "🟨⬜🟨⬜⬜", "Characters are in the wrong place"


@pytest.mark.parametrize(
    "answer,our_guess,expected_score",
    [
        pytest.param("adage", "adobe", "🟩🟩⬜⬜🟩", id="normal_guess1"),
        pytest.param("serif", "quiet", "⬜⬜🟨🟨⬜", id="normal_guess2"),
        pytest.param("raise", "radix", "🟩🟩⬜🟨⬜", id="normal_guess3"),
        pytest.param("abbey", "kebab", "⬜⬜🟩🟨🟨", id="multi_occur1"),
        pytest.param("abbey", "babes", "🟨🟨🟩🟩⬜", id="multi_occur2"),
        pytest.param("abbey", "abyss", "🟩🟩🟨⬜⬜", id="multi_occur3"),
        pytest.param("abbey", "algae", "🟩⬜⬜⬜🟨", id="multi_occur4"),
        pytest.param("abbey", "keeps", "⬜🟨⬜⬜⬜", id="multi_occur5"),
        pytest.param("abbey", "abate", "🟩🟩⬜⬜🟨", id="multi_occur6"),
    ],
)
@pytest.mark.xfail(reason="Not implemented yet")
def test_generic_score(answer, our_guess, expected_score):
    """Scenario Outline: Scoring guesses"""
    # Given a wordle <answer>
    # When scoring <guess>
    score = score_guess(our_guess, answer)
    # Then score should be <score>
    assert score == expected_score
