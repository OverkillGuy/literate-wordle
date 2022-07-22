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


-- Calculating entropy


SELECT count(*) FROM word_index; -- total number of accepted words: 12897
SELECT count(*) FROM answers_index; -- total number of answer words: 2315

-- Calculate the Information-Theory Entropy of a probability
-- Formula: log2(1/probability), with probability = float(num_occurences) / total
-- For an outcome happening 124 times over all answer words:
SELECT log2(1/ (124. /12897) ) AS entropy;

-- For solving Wordle, we want:
-- What is the number of answers that match this score for that guess
-- Aka what is the entropy = log 2 (1 / (number_valid_answers / total_num_answers))

-- Storing entropy as a table:
CREATE TABLE score_probability (
       guessidx int,
       scoreidx int,
       number_occurences int,
       entropy float,
       FOREIGN KEY(guessidx) REFERENCES word_index(wordidx),
       FOREIGN KEY(scoreidx) REFERENCES score_index(scoreidx)
);
-- TODO: Populate table, iterating over score_index but grouped by scoreidx
