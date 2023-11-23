#!/bin/bash

# We start by creating two folders
mkdir somedir1 somedir2
touch somefile{1..3}.txt

# Now filling this folders with our files
mv somefile* somedir1/
cp somedir1/somefile* somedir2/

# Now deleting one of the files
rm somedir1/somefile1.txt

# Finally, we can syncronyse both directories by
rsync -av somedir2/ somedir1/


