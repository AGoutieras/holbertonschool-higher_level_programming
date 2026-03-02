-- Lists all cities of California ordered by cities.id
-- Display cities of California using a subquery
SELECT name FROM hbtn_0d_usa.cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
