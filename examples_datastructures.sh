#!/bin/bash
#
## Bash list, called array:
#declare -a array=( "apple" "banana" "grape" )
#
## Looping through our array:
#for i in "${array[@]}"
#do
#	echo "This ${i} is delicious!"
#done
# Bash dictionary, called hash:
declare -A mealhash=([dinner]="steak" [lunch]="salad" [breakfast]="fruit")

# Looping through the dictionary:
for key in "${!mealhash[@]}"; do
	echo "For $key I like to eat: ${mealhash[$key]}"
done
