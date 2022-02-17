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
