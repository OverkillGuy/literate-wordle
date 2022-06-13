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
from literate_wordle.words import get_asset_zip_as_set


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
    ACCEPTED_WORDS = get_asset_zip_as_set("wordle_accepted_words_dict.txt.gz")
    ACCEPTED_WORDS_SIZE = len(ACCEPTED_WORDS)
    print(
        f"Dictionary is {ACCEPTED_WORDS_SIZE} words, "
        f"aka {log2(ACCEPTED_WORDS_SIZE)} bits for index"
    )

    SORTED_ACCEPTED_WORDS = sorted(list(ACCEPTED_WORDS))
    indexed_accepted_words = list(enumerate(SORTED_ACCEPTED_WORDS))

    dbcon = create_get_db()

    # First, create the tables
    create_table_sql = pkg_resources.read_text(db, "tables.sql")
    # PERF: Skipping cursor creation due to single-user nature, isolation is
    # useless, performance sought. See more in Python sqlite3 docs:
    # https://docs.python.org/3/library/sqlite3.html#using-sqlite3-efficiently
    dbcon.executescript(create_table_sql)

    dbcon.executemany(
        "INSERT INTO word_index(wordidx, word) values (?,?)", indexed_accepted_words
    )

    dbcon.commit()
    # Next is score indexes:
    ALL_SCORES = sorted(all_possible_scores())
    SCORES_SIZE = len(ALL_SCORES)

    print(
        f"Can get {SCORES_SIZE} possible scores "
        f"aka {log2(SCORES_SIZE)} bits of entropy on scores"
    )

    indexed_scores = list(enumerate(ALL_SCORES))

    dbcon.executemany(
        "INSERT INTO score_index(scoreidx, score) values (?,?)", indexed_scores
    )

    dbcon.commit()

    # TODO Insert scoring data in database too
    # Close is not a shortcut method and it's not called automatically,
    # so the connection object should be closed manually
    dbcon.close()
