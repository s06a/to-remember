# Table of Contents

<!-- vim-markdown-toc GFM -->

* [Git](#git)
	* [add server](#add-server)
	* [reset](#reset)
	* [branch, checkout](#branch-checkout)
		* [rename](#rename)
		* [delete/remove](#deleteremove)
	* [add/commit](#addcommit)
	* [ignore files](#ignore-files)
	* [revert](#revert)

<!-- vim-markdown-toc -->

# Git

## add server
to add the remote server to Git
```
git remote add origin remote_url
```

to confirm that the remote is added
```
git remote -v
```

to publish repo
```
git push -u origin branch_name
```

## reset
to remove or reset all added changes
```
git reset
```

to remove or reset added changes of a file
```
git reset filename
```

to unstage last commit
```
git reset HEAD~
```
```
git reset HEAD~1
```

## branch, checkout
create a new branch
```
git branch new_branch
```

switch branch
```
git checkout another_branch
```

create and switch branch
```
git checkout -b new_branch
```

merge (first checkout to main)
```
git merge old_branch
```
### rename
to rename current branch
```
git branch -m new_name
```

to rename a branch name
```
git branch -m old_name new_name
```

to rename main branch
```
git branch -M main
```


### delete/remove
to delete/remove a branch (locally)
```
git branch -d old_branch
```

to delete/remove a branch remotely
```
git push origin --delete remote_old_branch
```

to fetch list of remote branches and auto delete non remote branches
```
git fetch -p
```

list branches
```
git branch
```

fetch and work on a remote branch locally
```
git fetch origin
git checkout remote_branch
```

make a branch locally and push it to the remote server
```
git checkout -b new_branch
git push origin new_branch
```
```
git push –u origin branch_name
```

## add/commit
to add and commit changes only
```
git commit -am 'message'
```

to add changes only (modifications and deletions)
```
git add -u
```

to untrack a staged file
```
git rm --cached filename
```

## ignore files
git ignore (make a .gitignore file) [sample file](https://gist.github.com/octocat/9257657)

ignore files globally (make ~/.gitignore_global)
```
git config --global core.excludesfile ~/.gitignore_global
```

exclude local files (modify .git/info/exclude in local repository)

## revert
view and choose the commit id you want to revert
```
git log
```
to revert a commit by commit id
```
git revert commit_id
```
