#!/bin/bash
#
# This is the function basic structure
# function_name () {
#	command
# }

# Parameters
mimic () {
	echo "first parameter: $1" # see that what is different from another languages is that the parameters here are enumareted
	echo "second parameter: $2"
}

# Calling the mimic function, this will work only inside the bash script
# mimic 99 100

# Most complicated function
add () {
	num1=$1
	num2=$2
	result=$((num1+num2)) # ((_)) is used for arithmetic expressions and does not print out, differently from expr
	echo $result
}

# Assigning it to a variable without printing it out
output=$( add 15 30 ) # (_) tells bash to execute the operation in a subshell, so it does not print out
