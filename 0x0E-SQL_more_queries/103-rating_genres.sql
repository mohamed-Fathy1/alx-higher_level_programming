-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN (
    SELECT tv_shows.id, SUM(rate) AS rate
    FROM tv_shows JOIN tv_show_ratings
    ON tv_shows.id = tv_show_ratings.show_id
    GROUP BY tv_shows.id
) as Y ON Y.id = tv_show_genres.show_id
GROUP BY name
ORDER BY rating DESC;
