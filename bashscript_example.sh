#!/bin/bash
# <if you add -xv to the end of the above line, you use verbose mode, that is, almos everything that will be done will be communicated>
# Putting commands in the first lines is advised.
# Some functionalities to have in mind you be in the following lines.
# SET STRICT MODE: Causes shell to exit when a command fails
set -e
# # ??: Enables shell to print input lines as they are read
# set -v
# ??: Enales shell to print command traces (points out what the commands will do before doing it)
# set -x #comment: input will be shown with a plus sign in front, output without the plus sign

VARIABLE="one" # comment: example of a input
echo "This is a script variable: $VARIABLE"

