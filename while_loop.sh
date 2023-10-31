#!/bin/bash

echo "How many loops do you want?"
read LOOPS

COUNT=1
while [ $COUNT -le $LOOPS ]
do
	echo "We are at loop n. ${COUNT}."
	((COUNT++))
done
