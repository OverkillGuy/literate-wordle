-- Individually:
-- Guess word:
SELECT wordidx FROM word_index WHERE word = 'crane'; -- 2368
-- Score returned by Wordle:
SELECT scoreidx FROM score_index WHERE score = '⬜⬜🟨🟩⬜'; -- 15
-- Get answer index from guess index and score index:
SELECT answeridx FROM scores WHERE guessidx = 2368 AND scoreidx = 15;
-- Aggregated via (sub-optimal) JOINs:
-- Find answers for guess "crane" given its wordle score
SELECT answer.word FROM scores AS s
JOIN score_index AS si ON s.scoreidx = si.scoreidx
JOIN word_index as guess ON guess.wordidx = s.guessidx
JOIN word_index as answer ON answer.wordidx = s.answeridx
WHERE guess.word = 'crane' AND si.score = '⬜⬜🟨🟩⬜';
-- FIXME: Answer is picked from the ACCEPTED words list, not the subset that
-- matches the answers table!
