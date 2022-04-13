Feature: Track number of guesses
  As a Wordle game
  I need to track how many guesses were already given
  In order to announce win or game over

Scenario: First guess is allowed
  Given a wordle answer
  And I didn't guess before
  When I guess the word
  Then my guess is scored

Scenario: Sixth guess still allowed
  Given a wordle answer
  And I guessed 5 times
  When I guess the word
  Then my guess is scored

Scenario: Six failed guess is game over
  Given a wordle answer
  And I guessed 6 times already
  When I guess the word
  And my guess isn't the answer
  Then my guess is scored
  But game shows "Game Over"
  And game shows the real answer

Scenario: Winning guess
  Given a wordle answer
  And I guessed 3 times
  When I guess the word
  And my guess is the answer
  Then my guess is scored
  And score is perfect
  And game shows "Game Won"
