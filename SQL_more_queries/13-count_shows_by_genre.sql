-- Lists all genres and the number of shows linked to each
-- Display genre and number_of_shows ordered by number_of_shows descending
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
