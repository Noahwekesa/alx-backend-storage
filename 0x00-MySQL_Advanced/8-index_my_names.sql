-- sql that creates an index an index idx_my_names on the table names
--  and the letter of name and the score           

Create index idx_my_names on names(letter, score);
