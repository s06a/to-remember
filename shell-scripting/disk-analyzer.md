# Quetsion
Write a script to print free disk space in this format:
	Free/Total memory: 99G / 100G
	Percentage: 1 

# Answer
```bash
#!/bin/bash

a=( $(df -h /) )
echo "Free/Total memory: ${a[-3]} / ${a[-5]}
Percentage: ${a[-2]:0:-1}"
```

