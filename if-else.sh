#!/bin/bash

echo "What do you want to eat? "
read FOOD

if [ "$FOOD" = "pizza" ]; then
	echo "You will need a fork and a knife to eat your $FOOD."
elif [ "$FOOD" = "soup" ]; then
	echo "You will need a spoon to eat your $FOOD."
else
	echo "We do not have $FOOD available."
fi
