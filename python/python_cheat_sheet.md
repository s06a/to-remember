# Python Cheat Sheet

# Table of Contents

<!-- vim-markdown-toc GFM -->

* [basics](#basics)
* [pep8](#pep8)
* [control flow](#control-flow)
* [function](#function)
* [packages](#packages)
	* [virtual environment](#virtual-environment)

<!-- vim-markdown-toc -->

# basics

> strings are immutable

use raw strings
```
print(r'directory_name\another_folder\filename')
```

print multilines
```
print("""\
something: something_else
		-some_key	something_here
		-some_key	something_else_here
""")
```

concatenate strings
```
'2' + 2 * '0' + '2!'
```

concatenate strings with parentheses
```
print('hi'
      'there')
```

concatenate lists
```
[1, 2] + [3, 4]
> [1, 2, 3, 4]
```

lists are mutable
```
list[0] = 4
print(list[0])
> 4
```

empty part of list
```
list[2:8] = []
```

use end keyword to the newline in print
```
# in a loop
print(i, key=',')
> i, i+1, i+2
```

> sort lists the list ascending by default
```
list.sort(reverse=True)
```

# pep8
> 4 spaces instead of tabs

> max line character: 79

> space around operators and after commas

> `UpperCamelCase` for classes and `lowercase_with_underscores` for functions and methods

add whitespace around operators with the lowest priority
```
# correct forms
4*4 + 2 * (3+1)
(4+1) * (5-1) 
```

> two blank lines around top level functions and classes

> one blank line around methods inside class

# control flow

continue
```
for i in range(10):
	if i % 2 == 0:
		print(f'{i} is even')
		continue
	print(f'{i} is odd')
> 1 is odd
> 2 is even
> 3 is odd
...
```

match 
```
match something:
	case sub_something:
		return 'something'
	case somthing1 | something2 | something3:
		return 'something else'
	case _:
		return 'the other thing'
```

# function

default values in functions
```
i = 1

def func(n=i):
	return n

i = 2
print(func())
> 1
```

mutable objetcs in functions
```
def func(n, list=[]):
	list.append(n)
	return list

print(func(1))
> [1]
print(func(2))
> [1, 2]
```

positional arguments and keyword arguments
```
# positinal arguments
func(1, 2) # or as elements of iterable func(*(1, 2))

# keyword arguments
func(i=1, j=2) # or using a dictionary func(**{'i': 1, 'j': 2})
```
```
def func(n, *arguments, **keywords):
	print(n)
	[print(arg) for arg in arguments]
	[print(f'{kw}: {keywords[kw]}) for kw in keywords]

func(1, 2, 3, i=4, j=5)
> 1
> 2
> 3
> i: 4
> j: 5
```

unpacking positional arguments
```
args = [1, 3]
set(range(*args))
> {1, 2}
```

unpacking keyword arguments
```
dic1 = {"a": "b", "c": "d"}
func(**dic1)
```

lambda (anonymous function)
```
def power_to(n):
	return lambda x: x**n
p = power_to(10)
p(2)
> 1024
```
```
list = [('name1', 'James'), ('name2', 'Lilly'), ('name3', 'Harry')]
list.sort(key=lambda l:l[1])
[l[0] for l in list]
> ['name3', 'name1', 'name2']
```

# packages

## virtual environment
install the package
```
pip install virtualenv
```

create virtualenv
```
virtualenv name_of_the_venv
```

create venv in current folder
```
virtualenv .
```


specify python interpreter
```
virtualenv -p /path_to_python name_of_the_venv
```

activate venv
```
source bin/activate
```

deactivate venv
```
deactivate
```
