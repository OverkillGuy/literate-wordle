"""Score guesses of Wordle game"""


from collections import Counter


def score_guess(guess: str, answer: str) -> str:
    """Score an individual guess with Counter"""
    NO = "⬜"
    OK = "🟩"
    WRONG_PLACE = "🟨"
    # Counter("abbey") = Counter({'b': 2, 'a': 1, 'e': 1, 'y': 1})
    answer_chars = Counter(answer)
    response = ""
    for guess_char, answer_char in zip(guess, answer):
        if guess_char not in answer_chars:
            response += NO
            continue  # Early exit for this character, skip to next
        # From here on, we MUST have a char in common, regardless of place
        if answer_char == guess_char:
            response += OK
        elif answer_chars[guess_char] > 0:
            response += WRONG_PLACE
        # Either way, reduce occurence counter since we "used" this occurence
        answer_chars[guess_char] -= 1
        # No more hits = pretend character isn't even seen (remove from dict)
        if answer_chars[guess_char] == 0:
            del answer_chars[guess_char]
    return response
