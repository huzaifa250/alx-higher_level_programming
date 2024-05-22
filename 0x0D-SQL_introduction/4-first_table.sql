-- Creates a table called first_table with values id and name.
-- if the table not exists the script should not fail

CREATE TABLE IF NOT EXISTS `first_table` (`id` INT, `name` VARCHAR(256));
