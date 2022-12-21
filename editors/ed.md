# Table of Contents

<!-- vim-markdown-toc GFM -->

* [to open/insert/write/quit](#to-openinsertwritequit)
* [to view and navigate](#to-view-and-navigate)
* [to edit the buffer](#to-edit-the-buffer)

<!-- vim-markdown-toc -->

## to open/insert/write/quit

to open file
```
ed filename
```

to enable/disable printing error message
```
H
```

to see error message
```
h
```

to quit
```
q
```

to insert before the current line
```
i
```

to append after the current line
```
a
```

to close the insert mode
```
.
```

to write to a file
```
w filename
```

to read a file
```
r filename
```

## to view and navigate

to print whole the buffer
```
,p
```

to print lines between n and m
```
n,mp
```

to print lines with relative numbers n and m
```
-n,+mp
```

to print current line
```
p
```

to print line number and the content of the current line
```
n
```

to move to another line
```
line_number
```

## to edit the buffer

to edit the current line
```
s/word/target_word/
```

to change the current line in buffer
```
c
```

to change nth line
```
nc
```

to clear the buffer
```
,c
```

to delete line (n is the line number)
```
nd
```

to join lines (n and m are line numbers)
```
n,mj
```


