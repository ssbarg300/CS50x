SELECT name FROM people JOIN stars, movies ON  stars.person_id = people.id AND stars.movie_id = movies.id
WHERE movies.title = "Toy Story";

--SELECT name
--FROM people
--JOIN stars ON stars.person_id = people.id
--JOIN movies ON stars.movie_id = movies.id
--WHERE movies.title = 'Toy Story';