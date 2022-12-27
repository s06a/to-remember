#!/bin/bash

#Question
<< 'COMMENT'
get a name as a command line argument, reverse it, and say hello reversed!
COMMENT

#Answer
var="$1"
for (( i=${#var}; i>=0; i-- ))
do
	rev="$rev${var:$i:1}"
done

echo "Hello $rev!"
