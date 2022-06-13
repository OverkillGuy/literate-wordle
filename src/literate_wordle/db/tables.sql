-- Valid wordle words are 5 letter ASCII stored via UTF8 = 5 x 8 bits = 40 bits.
-- Use indexing tables (index, full version) to reduce that to log2(ACCEPTED_SIZE).
-- ACCEPTED_SIZE is order of 1e4 => log2(1e4) = 14 bits max ~ 30% original size.
CREATE table score_index (scoreidx int, score text);
-- Superset of all valid wordle words = accepted guesses
CREATE table word_index (wordidx int, word text);
-- Wordle answers = subset of accepted guesses, referencing word_index
CREATE table answers_index (wordidx int);
-- Computed score of a guess (word) against an answer (word), all via index
CREATE table scores (guessidx int, answeridx int, scoreidx int);
