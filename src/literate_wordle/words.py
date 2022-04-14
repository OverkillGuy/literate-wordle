"""Dictionary features to back wordle solutions"""

import gzip
import importlib.resources as pkg_resources
from functools import cache
from random import choice
from typing import Optional

from . import assets  # Relative import of the assets/ folder

ANSWERS_FILENAME = "wordle_answers_dict.txt.gz"
ACCEPTED_FILENAME = "wordle_accepted_words_dict.txt.gz"


def get_answers() -> set[str]:
    """Grab the Wordle answers as a set of string words"""
    return get_asset_zip_as_set(ANSWERS_FILENAME)


def get_accepted_words() -> set[str]:
    """Grab the Wordle accepted words dictionary as a set of string words"""
    return get_asset_zip_as_set(ACCEPTED_FILENAME)


@cache
def get_asset_zip_as_set(asset_filename: str) -> set[str]:
    """Decompress a file in assets module into a set of words, separated by newline"""
    compressed_bytes = pkg_resources.read_binary(assets, asset_filename)
    string = gzip.decompress(compressed_bytes).decode("ascii")
    string_list = [word.strip().lower().strip() for word in string.split("\n")]
    return set(string_list)


def pick_answer_word() -> str:
    """Pick a single word out of the dictionary of answers"""
    return choice(list(get_answers()))


def check_valid_word(guess: str) -> tuple[bool, Optional[str]]:
    """Check a wordle guess is valid: length and in dictionary"""
    answer_length = 5
    guess_length = len(guess)
    if guess_length < answer_length:
        return False, "Guess too short"
    elif guess_length > answer_length:
        return False, "Guess too long"
    valid_words_dict = get_accepted_words()
    if guess in valid_words_dict:
        return True, None
    return False, "Not a word from the dictionary"
