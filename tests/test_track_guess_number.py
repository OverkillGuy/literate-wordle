"""Validates the Gherkin file features/track_guesses.feature

Feature: Track number of guesses
  As a Wordle game
  I need to track how many guesses were already given
  In order to announce win or game over
"""


from literate_wordle.game import WordleGame, WordleMoveOutcome, play_round


def test_first_guess_allowed():
    """Scenario: First guess is allowed"""
    # Given a wordle answer
    answer = "orbit"
    # And I didn't guess before
    guess_number = 0
    game = WordleGame(answer=answer, guess_number=guess_number)
    # When I guess the word
    guess = "kebab"
    result = play_round(guess, game)
    # Then my guess is scored
    OUTCOME_CONTINUE = WordleMoveOutcome.GUESS_SCORED_CONTINUE
    assert result.outcome == OUTCOME_CONTINUE, "Game shouldn't be over yet"
    assert result.score is not None, "No score given as result"
    assert len(result.score) == 5, "Score of incorrect length"
    OK_CHARS = ["🟩", "🟨", "⬜"]
    assert all(
        char in OK_CHARS for char in list(result.score)
    ), "Score doesn't match score's characters"


def test_fifth_guess_allowed():
    """Scenario: Fifth guess still allowed"""
    # Given a wordle answer
    answer = "orbit"
    # And I guessed 4 times
    guess_number = 4
    game = WordleGame(answer=answer, guess_number=guess_number)
    # When I guess the word
    guess = "kebab"
    result = play_round(guess, game)
    # Then my guess is scored
    OUTCOME_CONTINUE = WordleMoveOutcome.GUESS_SCORED_CONTINUE
    assert result.outcome == OUTCOME_CONTINUE, "Game shouldn't be over yet"
    assert result.score is not None, "No score given as result"
    assert len(result.score) == 5, "Score of incorrect length"
    OK_CHARS = ["🟩", "🟨", "⬜"]
    assert all(
        char in OK_CHARS for char in list(result.score)
    ), "Score doesn't match score's characters"


def test_sixth_guess_fails_game():
    """Scenario: Sixth failed guess is game over"""
    # Given a wordle answer
    answer = "orbit"
    # And I guessed 5 times
    guess_number = 5
    game = WordleGame(answer, guess_number)
    # When I guess the word
    # And my guess isn't the answer
    guess = "kebab"
    result = play_round(guess, game)
    # Then my guess isn't scored
    assert result.outcome == WordleMoveOutcome.GAME_OVER_LOST, "Should have lost game"
    # But game shows "Game Over"
    assert "game over" in result.message.lower(), "Should show game over message"
    # And game shows the real answer
    assert answer in result.message


def test_winning_guess_wins():
    """Scenario: Winning guess"""
    # Given a wordle answer
    answer = "orbit"
    # And I guessed 3 times
    guess_number = 3
    game = WordleGame(answer, guess_number)
    # When I guess the word
    # And my guess is the answer
    guess = answer
    result = play_round(guess, game)
    # Then my guess is scored
    assert result.score is not None, "Guess should be scored"
    # And the score is perfect
    assert result.score == "🟩🟩🟩🟩🟩"
    # And game shows "Game Won
    assert result.outcome == WordleMoveOutcome.GAME_WON, "Should have won game"
    assert "game won" in result.message.lower()
