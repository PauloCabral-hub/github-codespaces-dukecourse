#!/bin/bash

# The first thing you need to do is update the database in order to use mlocate:
sudo updatedb

# The default locate search is case sensite. In order to make it otherwise:
locate -i <pattern>

# To locate files using find:
find . -name <pattern> # will find files in the current directory or bellow in which the name matches the pattern. Superuser permission may be necessary.

# Run the following command to compare the time of the two strategies
time / -name <pattern> && time locate <pattern>

# Run the following in the Github codespace
find . -name ".txt" | xargs grep <pattern> # it shows every occurence of the pattern in the file with the respective file.g

# Compare two approaches
time find . -name ".txt" | xargs grep <pattern> && time grep -R <pattern>
