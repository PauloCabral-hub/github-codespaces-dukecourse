#!/bin/bash

# To find a file with a given name in the current directory and sub-directories
find . -name "*.sh"

# To find in the current dir- and sub- of the pwd, objects in which there is a permission for execution, which are not invisible (! stands for not) and of the type file
find . -perm /+x ! -name '.*' -type f

# To exclude hidden directories, in the previous query
find . -perm /+x -not -path '*/\.*' -type f

# Obs.: it seems that \ works as a separation to the parser
