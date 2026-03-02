-- Creates and fills a table with 'id', 'name' and 'score' attributes.
-- Creates a table called second_table if it doesn't exist.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Fills the table with the id, name and score attributes.
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
