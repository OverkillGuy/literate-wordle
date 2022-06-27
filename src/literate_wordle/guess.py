"""Score guesses of Wordle game"""


from collections import Counter
from enum import Enum


class CharacterScore(str, Enum):
    """A single character's score"""

    OK = "🟩"
    NO = "⬜"
    WRONG_PLACE = "🟨"

    @classmethod
    @property
    def perfect_score(cls) -> str:
        """All-good Wordle score for perfect guess"""
        return "".join([cls.OK] * 5)


def score_guess(guess: str, answer: str) -> str:
    """Score an individual guess with Counter"""
    # Counter("abbey") = Counter({'b': 2, 'a': 1, 'e': 1, 'y': 1})
    answer_chars = Counter(answer)
    # NO is the default score, no need to detect it explicitly
    response: list[str] = [CharacterScore.NO] * len(answer)
    # First pass to detect perfect scores
    for char_index, (answer_char, guess_char) in enumerate(zip(guess, answer)):
        if answer_char == guess_char:
            response[char_index] = CharacterScore.OK
            answer_chars[guess_char] -= 1
    # Second pass for the yellows
    for char_num, (guess_char, existing_score) in enumerate(zip(guess, response)):
        if existing_score == CharacterScore.OK:
            continue  # It's already green: skip
        if answer_chars[guess_char] > 0:
            response[char_num] = CharacterScore.WRONG_PLACE
            # Reduce occurence counter since we "used" this occurence
            answer_chars[guess_char] -= 1
    return "".join(response)
