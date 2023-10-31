#!/bin/bash

# We are going to run a loop example

declare -a basket=("butter" "coffee" "sugar" "bread" "cheese")

# Now we perform a loop
for i in "${basket[@]}"
do 
	echo "${i} is in my basket."
done
