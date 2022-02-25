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

  Examples: Multiple occurences of same character
    | answer | guess	| score		|
    | abbey  | kebab	| ⬜🟨🟩🟨🟨	|
    | abbey  | babes	| 🟨🟨🟩🟩⬜	|
    | abbey  | abyss	| 🟩🟩🟨⬜⬜	|
    | abbey  | algae	| 🟩⬜⬜⬜🟨	|
    | abbey  | keeps	| ⬜🟨⬜⬜⬜	|
    | abbey  | abate	| 🟩🟩⬜⬜🟨	|
