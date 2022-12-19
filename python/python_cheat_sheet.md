# Python Cheat Sheet

# Table of Contents

<!-- vim-markdown-toc GFM -->

* [whitespace](#whitespace)
* [blank lines](#blank-lines)

<!-- vim-markdown-toc -->

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

## whitespace
add whitespace around operators with the lowest priority
```
# correct forms
4*4 + 2 * (3+1)
(4+1) * (5-1) 
```

## blank lines
> two blank lines around top leven functions and classes
> one blank line around methods inside class

