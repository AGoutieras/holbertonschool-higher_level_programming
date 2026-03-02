-- Lists all cities with their state name ordered by cities.id
-- Display cities and states using JOIN
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
