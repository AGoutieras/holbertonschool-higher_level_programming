-- Lists all cities of California ordered by cities.id
-- Display cities of California using a subquery
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
