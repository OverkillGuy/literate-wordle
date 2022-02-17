"""Validates the Gherkin file features/checking_guess_valid_word.feature:

Feature: Checking a guess is a valid word
  As a Wordle game
  I need to confirm each guessed word is valid
  So that I only accept real words, no kwyjibo

Scenario: Reject long words
  When guessing "affable"
  Then the guess is rejected
  And reason for rejection is "Guess too long"

Scenario: Reject short words
  When guessing "baby"
  Then the guess is rejected
  And reason for rejection is "Guess too short"

Scenario: Reject fake words via dictionary
  When guessing "vbpdj"
  Then the guess is rejected
  And reason for rejection is "Not a word from the dictionary"

Scenario: Accept five letter dictionary words
  When guessing "crane"
  Then the guess is accepted
"""

from literate_wordle.words import check_valid_word


def test_reject_long_words():
    """Scenario: Reject long words"""
    # When guessing "affable"
    guess = "affable"
    is_valid, reject_reason = check_valid_word(guess)
    # Then the guess is rejected
    assert not is_valid, "Overly long guess should have been rejected"
    # And reason for rejection is "Guess too long"
    assert reject_reason == "Guess too long"


def test_reject_overly_short_words():
    """Scenario: Reject short words"""
    # When guessing "baby"
    guess = "baby"
    is_valid, reject_reason = check_valid_word(guess)
    # Then the guess is rejected
    assert not is_valid, "Overly short guess should have been rejected"
    # And reason for rejection is "Guess too short"
    assert reject_reason == "Guess too short"


def test_reject_nondict_words():
    """Scenario: Reject fake words via dictionary"""
    # When guessing "vbpdj"
    guess = "vbpdj"
    is_valid, reject_reason = check_valid_word(guess)
    # Then the guess is rejected
    assert not is_valid, "Word not in dictionary should have been rejected"
    # And reason for rejection is "Not a word from the dictionary"
    assert reject_reason == "Not a word from the dictionary"


def test_accept_dict_words():
    """Scenario: Accept five letter dictionary words"""
    # When guessing "crane"
    guess = "crane"
    is_valid, reject_reason = check_valid_word(guess)
    # Then the guess is accepted
    assert is_valid, "Correct length word in dictionary should have been accepted"
    assert reject_reason is None, "Accepted word should have no reason to be rejected"
