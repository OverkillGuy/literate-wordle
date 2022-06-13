"""Statistical approach to solving Wordle, via brute-force pre-computation.

Use our score_guess function to compute (offline) all possible scores of all valid
guesses against all possible answers.

Use SQLite as database for computed values.
To minimize storage requirements, words and scores are replaced by their indexes.

Statistical analysis will be done in later phase in SQL, exploiting the data this file
provides.
"""


import importlib.resources as pkg_resources
import sqlite3
from itertools import product
from math import log2

from literate_wordle import db  # The db/ folder, for SQL scripts
from literate_wordle.guess import score_guess
from literate_wordle.words import (
    ACCEPTED_FILENAME,
    ANSWERS_FILENAME,
    get_asset_zip_as_set,
)


def entropy(occurences: int, total: int) -> float:
    """Compute the information-theory entropy of an event's occurence"""
    probability = float(occurences) / total
    return log2(1 / probability)


def all_possible_scores() -> list[str]:
    """Return a list of all possible Wordle scores, from combinatorics"""
    return ["".join(i) for i in product("🟩🟨⬜", repeat=5)]


def create_get_db():
    """Create or connect to the database"""
    return sqlite3.connect("wordle_solve.db")


if __name__ == "__main__":
    ACCEPTED_WORDS = get_asset_zip_as_set(ACCEPTED_FILENAME)
    ACCEPTED_WORDS_SIZE = len(ACCEPTED_WORDS)
    print(
        f"Accepted dict is {ACCEPTED_WORDS_SIZE} words, "
        f"aka {log2(ACCEPTED_WORDS_SIZE)} bits for index"
    )

    SORTED_ACCEPTED_WORDS = sorted(list(ACCEPTED_WORDS))
    indexed_accepted_words = list(enumerate(SORTED_ACCEPTED_WORDS))
    accepted_word_index_dict = {word: index for index, word in indexed_accepted_words}

    dbcon = create_get_db()

    # First, create the tables
    create_table_sql = pkg_resources.read_text(db, "tables.sql")
    # PERF: Skipping cursor creation due to single-user nature, isolation is
    # useless, performance sought. See more in Python sqlite3 docs:
    # https://docs.python.org/3/library/sqlite3.html#using-sqlite3-efficiently
    dbcon.executescript(create_table_sql)

    dbcon.executemany(
        "INSERT INTO word_index(wordidx, word) VALUES (?,?)", indexed_accepted_words
    )

    dbcon.commit()
    # Next is score indexes:
    ALL_SCORES = sorted(all_possible_scores())
    SCORES_SIZE = len(ALL_SCORES)

    print(
        f"Scores list is {SCORES_SIZE} items "
        f"aka {log2(SCORES_SIZE)} bits for index"
    )

    indexed_scores = list(enumerate(ALL_SCORES))
    scores_index_dict = {score: index for index, score in indexed_scores}
    dbcon.executemany(
        "INSERT INTO score_index(scoreidx, score) VALUES (?,?)", indexed_scores
    )

    dbcon.commit()
    # Now for the ANSWERS, not just accepted
    ANSWER_WORDS = get_asset_zip_as_set(ANSWERS_FILENAME)
    ANSWER_WORDS_SIZE = len(ANSWER_WORDS)
    print(
        f"Answers dict is {ANSWER_WORDS_SIZE} words, "
        f"aka {log2(ANSWER_WORDS_SIZE)} bits for index"
    )

    SORTED_ANSWER_WORDS = sorted(list(ANSWER_WORDS))
    # Index not contiguous, but via accepted_words indexes above
    answer_word_acceptindex_dict = {
        word: accepted_word_index_dict[word] for word in SORTED_ANSWER_WORDS
    }
    # As a list of list-of-1-item for SQL insertion via executemany
    answer_word_acceptindexes = [
        [index] for _, index in answer_word_acceptindex_dict.items()
    ]
    dbcon.executemany(
        "INSERT INTO answers_index(wordidx) VALUES (?)", answer_word_acceptindexes
    )
    dbcon.commit()

    # Insert scoring data
    # TODO iterate over guess
    guess = "crane"
    guess_index = accepted_word_index_dict[guess]


    # for answer in SORTED_ANSWER_WORDS: ...

    # Relying on dict iteration order being dict insertion order (!!!)
    answer_indexes =  list(answer_word_acceptindex_dict.values())
    scores = [score_guess(guess, answer) for answer in SORTED_ANSWER_WORDS]
    score_indexes= [scores_index_dict[score] for score in scores]
    # print(
    #     f"Score for {guess=}({guess_index=}) against {answer=}({answer_index=}): "
    #     f"{score=}({score_index=})"
    # )
    #
    # We HAVE 3 x long arrays, one for each structure: ([guesses], [answer], [scores])
    # We NEED a long array of TRIPLES [(guess1, answer1, score1), (guess2, answer2, score2),]
    # Classic problem of structure-of-array vs array-of-structure:
    array_of_structure_score = [(guess_index, answer_index, score_index) for answer_index, score_index in zip(answer_indexes, score_indexes)]
    dbcon.executemany(
        "INSERT INTO scores(guessidx, answeridx, scoreidx) VALUES (?,?,?)", array_of_structure_score
    )
    dbcon.commit()
    # Close is not a shortcut method and it's not called automatically,
    # so the connection object should be closed manually
    dbcon.close()
