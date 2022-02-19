Feature: Scoring guesses
  As a Wordle game
  I need to tell the player how good their guess is
  In order to help them find the proper answer

Background:
  Given a guess that's a valid dictionary word

Scenario: Perfect guess gives perfect score
  Given a wordle answer "crane"
  When scoring the guess "crane"
  Then score should be "🟩🟩🟩🟩🟩"

Scenario: No character in common
  Given a wordle answer "brave"
  When scoring the guess "skill"
  Then score should be "⬜⬜⬜⬜⬜""
