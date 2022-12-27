# Table of Contents

<!-- vim-markdown-toc GFM -->

* [Shell Commands](#shell-commands)
	* [work as root](#work-as-root)
	* [jobs](#jobs)
	* [password](#password)
	* [Shell and defaults](#shell-and-defaults)
	* [info and manual](#info-and-manual)
	* [network commands](#network-commands)
	* [directory and files](#directory-and-files)
	* [Pipe and redirecting](#pipe-and-redirecting)
	* [print](#print)
	* [to shift](#to-shift)
	* [type](#type)
* [handy commands](#handy-commands)
	* [list name of the files in a directory](#list-name-of-the-files-in-a-directory)
* [Shell Scripting](#shell-scripting)
	* [to comment](#to-comment)
	* [if elif else](#if-elif-else)
	* [for loop](#for-loop)
	* [while](#while)
	* [until](#until)
	* [case](#case)

<!-- vim-markdown-toc -->

# Shell Commands

## work as root
if root password is set
```
su
```
run command as root with su
```
su -c 'ls -l'
```
if root password doesn't exist
```
sudo bash
```
```
sudo -i
```

exit root
```
exit
```

## jobs
to suspend a job: `ctrl`+`z`

to list jobs
```
jobs
```

to bring back a job
```
fg n
```

to terminate a job
```
kill -TERM %n
```

## password
to change password
```
passwd user
```

## Shell and defaults
current shell
```
echo $SHELL
```
```
ps
```

to change shell
```
chsh -s shell_path username
```

to change the default editor
```
sudo update-alternatives --config editor
```


## info and manual
to see manual of a command
```
man command
```
to see help and scroll
```
command --help | less
```

short description of a command
```
whatis command
```

system name
```
hostname
```

to get system information
```
uname -a
```

to see date
```
date
```

to see how much disk is free (human readable)
```
df -h
```

to see command history
```
history
```

to repeat the last command
```
!!
```

to select a command from history list (n is the line number of prefered command)
```
!n
```

to see or use the last argument of the last command
```
!$
```

## network commands
to ping an ip address
```
ping ip_address
```

## directory and files
to see where you are
```
pwd
```

to copy a file (cp overwrites even if there's a file! so, use it interactively)
```
cp -i filename1 filename2
```

to move or rename a file (like cp, it also overwrites)
```
mv -i filename1 filename2
```

to search in a file (`-w` to search for whole words)
```
grep 'word' filename
```

display the beginning of a file (`-n` to limit row numbers to n)
```
head filename
```

display the tail of a file (`-n` to limit row numbers to n, `-f` to follow data as it updates)
```
tail filename
```

display a file in order (`-n` with numbers, `-u` no duplicates)
```
sort filename
```

to compare two files
```
diff -u filename1 filename2
```

to identify the contents of a file
```
file filename
```

to list files and sub-directories
```
ls
```
```
echo *
```

to list files and show permissions
```
ls -l
```

to search in directory
```
ls 01*.md
```

to list invisible files
```
ls -a
```

to make directory with parent directories
```
mkdir -p dirname
```

to remove directory
```
rmdir dirname
```
```
rm -r
```

to change permissions (u:user, g:group, o:other) [-rwx(u)rwx(g)rwx(o)]
```
chmod o+wx,u-rx,g=r filename
ls -l filename
> --w-r--rwx
```

to change permissions using absolute permissions (0: Np, 1:Ep, 2:Wp, 4:Rp)
```
chmod 750 filename
> -rwxr-x---
```

to change ownership
```
chown user filename
```

to change group ownership
```
chgrp group filename
```

give permissions of the owner to user and group
```
chmod ug+s dirname
```

## Pipe and redirecting
```
sort filename | head -4
```

send tail of a file to printer
```
tail filename | lpr
```

create a file by redirecting output of echo
```
ehco 'This is a test!' > filename
```

## print
```
echo $list # seperates by IFS (space, tab, newline)
echo "$list"
```

```
printf "%s\n%d\n%b\n" "12\n45" 12 "hi\nthere"
> 12\n45
> 12
> hi
> there
```

display file
```
cat filename
```

counting words in a file
```
wc filename
> n_lines n_words n_bytes filename
```

## to shift
```
set 1 2 3
echo "$* length:$#"
shift
echo "$* length:$#"
> 1 2 3 3
> 2 3 2
```

## type
to find out if command is a shell builtin or not

# handy commands

## list name of the files in a directory
```
ls -l | grep -o -E '[^ ]+$'
```

# Shell Scripting

## to comment

single line comment
```
# comment
```

multi line commment
```
<< 'COMMENT'
write your
comment in
a multi line
style
COMMENT
```
 
## if elif else
```
if [ statement ]
then
	commands
elif [ statement ]
then
	commands
else
	commands
fi
```

## for loop
```
for variable in list
do
	commands
done
```

## while
```
while something_true
do
	commands
done
```

## until
```
until something_true
do
	commands
done
```

## case
```
case $var in
1st_match)
	commands
	;;
nth_match)
	commands
	;;
*) # this one is optional
	commands
	;;
esac
```
