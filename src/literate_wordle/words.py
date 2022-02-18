"""Dictionary features to back wordle solutions"""

import gzip
import importlib.resources as pkg_resources
from functools import cache
from random import choice
from typing import Optional, Tuple

from . import assets  # Relative import of the assets/ folder


@cache
def get_asset_zip_as_set(asset_filename: str) -> set[str]:
    """Decompress a file in assets module into a set of words, separated by newline"""
    compressed_bytes = pkg_resources.read_binary(assets, asset_filename)
    string = gzip.decompress(compressed_bytes).decode("ascii")
    string_list = [word.strip().lower() for word in string.split("\n")]
    return set(string_list)


def pick_answer_word() -> str:
    """Pick a single word out of the dictionary of answers"""
    return choice(list(get_asset_zip_as_set("wordle_answers_dict.txt.gz")))


def check_valid_word(guess: str) -> Tuple[bool, Optional[str]]:
    """Check wordle guess length only, no dict checks"""
    answer_length = 5
    guess_length = len(guess)
    if guess_length < answer_length:
        return False, "Guess too short"
    elif guess_length > answer_length:
        return False, "Guess too long"
    valid_words_dict = get_asset_zip_as_set("wordle_accepted_words_dict.txt.gz")
    if guess in valid_words_dict:
        return True, None
    return False, "Not a word from the dictionary"
