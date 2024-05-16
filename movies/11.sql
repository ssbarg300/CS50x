SELECT title FROM movies JOIN stars, people, ratings ON stars.movie_id = movies.id AND stars.person_id = people.id
WHERE people.name = "Chadwick Boseman"
AND ratings.movie_id = movies.id
ORDER BY ratings.rating DESC LIMIT 5;