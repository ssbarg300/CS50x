SELECT COUNT(movies.title) AS n
FROM movies INNER JOIN ratings ON ratings.movie_id = movies.id
WHERE ratings.rating = 10.0;