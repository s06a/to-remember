# Table of Contents
<!-- vim-markdown-toc GFM -->

* [working with vi/vim](#working-with-vivim)
	* [to open a file](#to-open-a-file)
	* [to see help](#to-see-help)
	* [command mode](#command-mode)
	* [normal mode](#normal-mode)
	* [run shell command](#run-shell-command)
	* [to work with multiple files](#to-work-with-multiple-files)
	* [to work with tabs](#to-work-with-tabs)
	* [to work with split screen mode](#to-work-with-split-screen-mode)
	* [to write (insert mode)](#to-write-insert-mode)
	* [to copy/cut/paste/mark](#to-copycutpastemark)
	* [to save or exit](#to-save-or-exit)
	* [to navigate in the editor](#to-navigate-in-the-editor)
	* [to delete content](#to-delete-content)
	* [to undo](#to-undo)
	* [to find, or find and replace a word](#to-find-or-find-and-replace-a-word)
* [plugins](#plugins)
	* [install plugin with Vundle plugin manager](#install-plugin-with-vundle-plugin-manager)
	* [generate table of contents for md files](#generate-table-of-contents-for-md-files)
	* [NERDTree - file system explorer in vim](#nerdtree---file-system-explorer-in-vim)
	* [vim-fugitive - use Git inside vim](#vim-fugitive---use-git-inside-vim)
	* [ale - to autofix writing issues](#ale---to-autofix-writing-issues)

<!-- vim-markdown-toc -->

# working with vi/vim

## to open a file
```
vi filename
```

## to see help
```
:help
```

## command mode
```
:
```

## normal mode
```
esc
```

## run shell command
```
:!shell_command
```

## to work with multiple files
to open multiple files
```
vi file1 file2 file3
```

go to the next file
```
:n
```

go to the previous file
```
:N
```

to list all opened files (buffers)
```
:ls
```

to select buffer file (n is number of prefered buffer)
```
:b n
```

go to the next buffer
```
:bn
```

go to the previous buffer
```
:bp
```

to close current buffer
```
:bd
```

to save all files and quit
```
:wqa
```

to discard all changes and quit
```
:q!
```

## to work with tabs
to create/open a file in a new tab
```
:tabe filename
```

to open multiple files in tab mode from terminal
```
vim -p file1 file2
```

to move to the next tab
```
:tabn
```
```
gt
```
to move to the previous tab
```
:tabp
```
```
gT
```

## to work with split screen mode
to create/open a file with split screen
```
:sp filename
```

to open a file with horizontal split
```
:split filename
```

to opne a file with vertical split
```
:vsplit filename
```

to move to the bottom screen (`ctrl`+`w` and then)
```
w
```

to move to the top screen (`ctrl`+`w` and then)
```
W
```

to navigate between splitted screens (`ctrl`+`w` and then)
```
arrow keys
```

to increase/decrease height
```
ctrl+w +/-
```

to increase/decrease width
```
ctrl+w >/<
```

to equalize height and width of all windows
```
ctrl+w =
```

## to write (insert mode)
insert
```
i
```
jump and insert at the beginning of the current line
```
I
```
append (insert after current cursor)
```
a
```
jump and append at the end of the current line
```
A
```
insert a new line after the current line
```
o
```
insert a new line before the cuurent line
```
O
```

## to copy/cut/paste/mark 
copy a line
```
yy
```
copy a word
```
yw
```
paste
```
p
```
cut line (also works as delete the line)
```
dd
```
cut word (also works as delete the word)
```
dw
```
select (move cursor, use `y` to copy and `d` to cut, use `p` to paste)

```
v
```

to set a marker named 'f'
```
`m` then `f`
```

to jump to the marker 'f'
```
`'` then `f`
```

## to save or exit 

save and quit
```
ZZ
```

discard changes and quit
```
:q!
```

just save
```
:w
```

save and quit
```
:wq
```

## to navigate in the editor 
move the cursor
```
Arrow keys
```
move cursur to the beginning of the current line
```
^
```
move cursor to the end of the current line
```
$
```
jump to the first line
```
gg
```
jump to the last line
```
G
```
move to the next word
```
w
```
move to the previous word
```
b
```

## to delete content 

delete a single character
```
x
```
delete the current line
```
dd
```

## to undo 

undo the last change
```
u
```
undo all changes
```
U
```

## to find, or find and replace a word 
to search for a word forward (press `enter` then press `n` to jump to the next match and `N` to jump to the previous match)
```
/word
```

to search for a word backward (press `enter` then press `n` to jump to the next match and `N` to jump to the previous match)
```
?word
```

to search for a whole word (press `enter` then press `n` to jump to the next match and `N` to jump to the previous match)
```
/\<word\>
```

to search for a whole word (case insensitive) (press `enter` then press `n` to jump to the next match and `N` to jump to the previous match)
```
/\<word\>\c
```

to find and replace all matches
```
:%s/word/target_word/g
```

to find and replace with confirmation
```
:%s/word/target_word/gc
```

to find whole word and replace
```
:%s/\<word\>/target_word/g
```

to find and replace (case insensitive)
```
:%s/word/target_word/gi
```

to find and replace in the current line
```
:s/word/target_word/g
```

to find and replace in certain lines
```
:(start_line_number),(end_line_number)s/word/target_word/g
```

# plugins

## install plugin with Vundle plugin manager 

add plugin install line in vimrc
```
Plugin 'sample_plugin'
```
```
:so $MYVIMRC
```
```
:PluginInstall
```

## generate table of contents for md files
install [vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc)

generate table of contents for GFM
```
:GenTocGFM
```

update toc
```
:UpdateToc
```

remove toc
```
:RemoveToc
```

## NERDTree - file system explorer in vim
install [NERDTree](https://github.com/preservim/nerdtree)

enable NERDTree (use `ctrl`+`w` and arrow keys to navigate between splits)
```
:NERDTree
```

to open a file in vertical split
```
s
```

change the CWD to the selected dir
```
cd
```

change tree root to selected dir
```
CD
```

refresh directory
```
r
```

close the NERDTree
```
q
```

toggle help
```
?
```

open a file in new tab
```
t
```

move to the next tab
```
gt
```

move to the previous tab
```
gT
```
## vim-fugitive - use Git inside vim
install [vim-fugitive](https://github.com/tpope/vim-fugitive)

```
:Git command
```

## ale - to autofix writing issues
install [ale](https://github.com/dense-analysis/ale)

make pep8 available for python files
```
" make and open this file: ~/.vim/ftplugin/python.vim
" add below lines and save the file, reopen vim

let b:ale_fixers = {'python': ['autopep8', 'isort', 'remove_trailing_lines', 'trim_whitespace', 'autoflake', 'add_blank_lines_for_python_control_statements']}

" to enable autofix on save
let g:ale_fix_on_save = 1
```

to see appropriate fixers for a file
```
:ALEFixSuggest
```
