"""Command line entrypoint for pywordle"""


import argparse
import sys
from typing import Optional, Sequence

from literate_wordle.main import new_game, play_game


def parse_args(raw_args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse given command line arguments"""
    description = "Wordle implementation in Python, as literate programming"
    # Bit overkill since there is no real argument to parse yet
    parser = argparse.ArgumentParser(prog="pywordle", description=description)
    return parser.parse_args(raw_args)


def play_game_args(raw_args: Optional[Sequence[str]] = None):
    """Play a standard Wordle game from stdin to stdout, given args"""
    _ = parse_args(raw_args)
    game = new_game()
    play_game(game=game, guess_fetcher=input, response_logger=print)


def main():
    """Pass sys.argv to the play_game_args function"""
    play_game_args(sys.argv[1:])
