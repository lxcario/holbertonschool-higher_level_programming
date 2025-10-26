-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT
    name
FROM
    tv_genres AS g
INNER JOIN
    tv_show_genres AS m
ON
    g.id = m.genre_id
INNER JOIN
    tv_shows t
ON
    m.show_id = t.id
WHERE
    t.title = 'Dexter'
ORDER BY
    name ASC;
