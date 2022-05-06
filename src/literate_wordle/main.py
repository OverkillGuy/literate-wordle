"""Entrypoint for pywordle"""


from typing import Callable

from literate_wordle.game import WordleGame, WordleMoveOutcome, play_round
from literate_wordle.words import pick_answer_word


def new_game() -> WordleGame:
    """Generate a new WordleGame"""
    return WordleGame(answer=pick_answer_word(), guess_number=1)


def play_game(game: WordleGame, guess_fetcher: Callable, response_logger: Callable):
    """Plays the given WordleGame until completion.

    Asks guess_fetcher for guess, and sends response to response_logger
    """
    outcome = WordleMoveOutcome.GUESS_SCORED_CONTINUE  # Gotta start somehow
    while outcome not in {WordleMoveOutcome.GAME_WON, WordleMoveOutcome.GAME_OVER_LOST}:
        guess = guess_fetcher()
        result = play_round(guess=guess, game=game)
        response_logger(result.message)
        game = result.game
        outcome = result.outcome
