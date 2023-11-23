#!/bin/bash

# For finding differences in structure of two files
diff <file1> <file2>

# To find unique line entries in a given file
uniq <file1>

# To sort the file
sort <file1>

# Interesting way to look at the last column of a .csv file
cat <file1> | rev | cut -d, -f1 | rev

# For very large files, you can use the following command to shuffle lines
shuf -n 10 <file1>

# grep can also be used with regex for very powerful utilities see: https://en.wikipedia.org/wiki/Regular_expression#:~:text=A%20regular%20expression%20(shortened%20as,strings%2C%20or%20for%20input%20validation.

# For uppercase or lowercase strings
tr a-z A-Z <file or string>

# For making substitutions
sed 's/<pattern_to_substitute>/<new_pattern>'

# If you wanna see the results based on some condition, you can use the AWK language aid. Ex.:
awk 'NF < 10' # shows the results if the number or results is less than 10