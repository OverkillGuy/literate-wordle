"""Wordle game's state and playing rounds"""


from dataclasses import dataclass
from enum import Enum
from typing import Optional

from literate_wordle.guess import score_guess
from literate_wordle.words import check_valid_word


class WordleMoveOutcome(Enum):
    """Outcome of a single move"""

    GAME_OVER_LOST = 1
    GAME_WON = 2
    GUESS_SCORED_CONTINUE = 3
    GUESS_NOTVALID_CONTINUE = 4


@dataclass
class WordleGame:
    """A Wordle game's internal state, before a move is played"""

    answer: str
    guess_number: int


@dataclass
class WordleMove:
    """A Wordle game state once a move is played"""

    game: WordleGame
    outcome: WordleMoveOutcome
    message: str
    score: Optional[str]


def play_round(guess: str, game: WordleGame) -> WordleMove:
    """Use guess on the given game, resulting in WordleMove"""
    if game.guess_number >= 6:
        message = f"Too many guesses: Game Over. Answer was: {game.answer}"
        outcome = WordleMoveOutcome.GAME_OVER_LOST
        return WordleMove(game=game, outcome=outcome, message=message, score=None)
    valid, validity_msg = check_valid_word(guess)
    if not valid and validity_msg is not None:
        outcome = WordleMoveOutcome.GUESS_NOTVALID_CONTINUE
        return WordleMove(game=game, outcome=outcome, message=validity_msg, score=None)
    # Guess now guaranteed to be valid: count it
    game.guess_number += 1
    score = score_guess(guess, game.answer)
    if score == "🟩🟩🟩🟩🟩":
        outcome = WordleMoveOutcome.GAME_WON
        message = f"Correct! Game won in {game.guess_number - 1} guesses"
        return WordleMove(game=game, outcome=outcome, message=message, score=score)
    # Only case left is "try another guess"
    outcome = WordleMoveOutcome.GUESS_SCORED_CONTINUE
    message = f"Try again! Guess number {game.guess_number - 1}. Score is: {score}"
    return WordleMove(game=game, outcome=outcome, message=message, score=score)
