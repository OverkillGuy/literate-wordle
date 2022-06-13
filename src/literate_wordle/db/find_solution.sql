-- Guess word:
SELECT wordidx FROM word_index WHERE word = 'crane'; -- 2368
-- Score returned by Wordle:
SELECT scoreidx FROM score_index WHERE score = "⬜⬜🟨🟩⬜"; -- 15
-- Get answer index from guess index and score index:
SELECT answeridx FROM scores WHERE guessidx = 2368 AND scoreidx = 15;
-- Pivoting to words:
SELECT word_index.word
FROM scores
INNER JOIN word_index ON wordidx = answeridx
WHERE guessidx = 2368 AND scoreidx = 15;
-- TODO: Replace hardcoded guess/score index with subquery
-- See this obsoleted sample:
-- -- SELECT * from score_by_secrets as s join word_by_index as w on w.wordnum = s.secret WHERE w.word = "crane";
