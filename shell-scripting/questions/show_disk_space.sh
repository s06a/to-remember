#!/bin/bash

# Question
<< 'COMMENT'
Write a script to print free disk space percentage in this format:

Percentage: 15
COMMENT

# Answer
var=( $(df -h /) )
echo "Percentage: ${var[-2]:0:-1}"
