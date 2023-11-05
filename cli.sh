#!/bin/bash
#
# example for running the script: 
# ./cli.sh --count 5 --phrase "toc toc"

# A. Core: contains the functionality
# Print out the second argument N times where N is the first argument
phrase_generator () {
	for ((i=0; i<$1 ; i++ )) ; do
		echo "$2"
	done
}

# B. Parser: parses the arguments
while [[ $# -gt 1 ]] # this <strange variable> gets the number of inputs to the CLI
do
	key="$1"
	case $key in
	       	-c | --count)
			COUNT="$2"
			shift # this shifts the first argument to be the second and makes the strange variable decrement by 1
		;;
		-p | --phrase)
			PHRASE="$2"
			shift
		;;
	esac
			shift

done

# C. Entry: passes the input to the function
phrase_generator "${COUNT}" "${PHRASE}"

