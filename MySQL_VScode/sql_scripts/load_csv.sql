-- To run this query, client and server sides must allow loading local data
-- NEI - how to do this
LOAD DATA LOCAL INFILE  'ratings.csv' INTO TABLE ratings
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
(@designation,@points,@province) set name=@name,rating=@points,region=@province;