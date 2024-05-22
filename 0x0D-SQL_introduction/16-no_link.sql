-- Lists all records of the table second_table have a name value.
-- Records are ordered by descending score.

SELECT score, name FROM second_table
WHERE CHAR_LENGTH(name) > 0 
ORDER BY score DESC
