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
    response: dict[int, str] = {}
    # First pass to detect perfect scores
    perfect_scores = [
        answer_char == guess_char for guess_char, answer_char in zip(guess, answer)
    ]
    for char_index, is_score_perfect in enumerate(perfect_scores):
        if is_score_perfect:
            response[char_index] = CharacterScore.OK
            answer_chars[guess[char_index]] -= 1
    # Now the non-perfects
    for char_num, (guess_char, _answer_char) in enumerate(zip(guess, answer)):
        if char_num in response:
            continue  # No point scoring this one, we got it already as perfect
        if guess_char not in answer_chars or answer_chars[guess_char] == 0:
            response[char_num] = CharacterScore.NO
            continue  # Early exit for this character, skip to next
        # From here on, we MUST have a char in common, regardless of place
        elif answer_chars[guess_char] > 0:
            response[char_num] = CharacterScore.WRONG_PLACE
        # Either way, reduce occurence counter since we "used" this occurence
        answer_chars[guess_char] -= 1
    return "".join([response[i] for i in range(5)])
