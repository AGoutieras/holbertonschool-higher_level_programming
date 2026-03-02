-- Lists all records of the table second_table without NULL names.
-- Display score and name ordered by descending score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;