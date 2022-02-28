"""Wordle game's state and playing rounds"""


from dataclasses import dataclass
from enum import Enum
from typing import Optional


class WordleMoveOutcome(Enum):
    """Outcome of a single move"""

    GAME_OVER_LOST = 1
    GAME_WON = 2
    GUESS_SCORED_CONTINUE = 3


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
    result = WordleMoveOutcome.GAME_OVER_LOST
    return WordleMove(game=game, outcome=result, message="You suck!", score=None)
