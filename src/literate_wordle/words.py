"""Dictionary features to back wordle solutions"""

import gzip
import importlib.resources as pkg_resources
from random import choice
from typing import Optional, Tuple

from . import assets  # Relative import of the assets/ folder


def get_words_list() -> list[str]:
    """Decompress the wordle dictionary"""
    dict_compressed_bytes = pkg_resources.read_binary(
        assets, "wordle_answers_dict.txt.gz"
    )
    dict_string = gzip.decompress(dict_compressed_bytes).decode("ascii")
    answer_word_list = [word.strip().lower() for word in dict_string.split("\n")]
    return answer_word_list


def pick_answer_word() -> str:
    """Pick a single word out of the dictionary of answers"""
    return choice(get_words_list())


def check_valid_word(guess: str) -> Tuple[bool, Optional[str]]:
    """Check wordle guess length only, no dict checks"""
    answer_length = 5
    guess_length = len(guess)
    if guess_length < answer_length:
        return False, "Guess too short"
    elif guess_length > answer_length:
        return False, "Guess too long"
    return True, None  # No dictionary check
