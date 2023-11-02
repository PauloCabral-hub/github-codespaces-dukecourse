#!/bin/bash

echo "How many lines do you want?"
read LINES

declare -a array=("apple" "banana" "grapes")

COUNT=1
while [ $COUNT -le $LINES ]
do
	rand=$[ $RANDOM % 3 ]  # here the first operator is the modulos, using expression helps
	echo "$COUNT ${array[ $rand ]} " >> sampling_example.txt
	((COUNT++))
done
