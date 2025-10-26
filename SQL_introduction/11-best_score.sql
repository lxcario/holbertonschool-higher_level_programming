-- A script that lists records with a score >= 10 of the table second_table.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
