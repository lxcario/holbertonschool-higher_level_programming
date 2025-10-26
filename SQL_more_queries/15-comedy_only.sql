-- A script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT
    title
FROM
    tv_shows AS t
INNER JOIN
    tv_show_genres AS m
ON
    t.id = m.show_id
INNER JOIN
    tv_genres AS g
ON
    m.genre_id = g.id
WHERE
    g.name = 'Comedy'
ORDER BY
    title ASC;
