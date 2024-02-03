USE ratings;
(SELECT 'name', 'rating', 'region' FROM ratings)
UNION
SELECT * FROM ratings
INTO OUTFILE '/home/paulo-cabral/Documents/MySQL_VScode/sql_scripts/table.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

-- OUTPUT
-- Error: ER_OPTION_PREVENTS_STATEMENT: The MySQL server is running with the --secure-file-priv option so it cannot execute this statement