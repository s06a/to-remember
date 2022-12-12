#!/bin/bash

# Question
<< 'COMMENT'
Write a script to print free disk space in this format: 
	Free/Total memory: 99G / 100G 
	Percentage: 1
COMMENT

# Answer
var=( $(df -h /) )
echo "Free/Total memory: ${var[-3]} / ${var[-5]}
Percentage: ${var[-2]:0:-1}"
