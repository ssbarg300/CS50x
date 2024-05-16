SELECT DISTINCT people.name
FROM people
JOIN stars ON stars.person_id = people.id
JOIN movies ON stars.movie_id = movies.id
JOIN stars AS s2 ON s2.movie_id = movies.id
JOIN people AS p2 ON s2.person_id = p2.id
WHERE p2.name = "Kevin Bacon" AND p2.birth = "1958" AND people.name != "Kevin Bacon";