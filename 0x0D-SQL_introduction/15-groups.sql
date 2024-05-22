-- Lists the number of records with the same score from the table second_table
-- Sorted by the number of records (descending).

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score ORDER BY number DESC;
