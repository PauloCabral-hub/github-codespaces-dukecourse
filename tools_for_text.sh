#!/bin/bash

# For finding differences in structure of two files
diff <file1> <file2>

# To find unique line entries in a given file
uniq <file1>

# To sort the file
sort <file1>

# Interesting way to look at the last column of a .csv file
cat <file1> | rev | cut -d, -f1 | rev