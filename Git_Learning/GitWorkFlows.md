# Setup Of Git

A. Config to user / Your Identity
+ $ git config --global user.name 'Nitin Shinde'
+ $ git config --global user.email '@cloud'

B. To View all the settings
+ $ git config --list --show-origin

C. Checking your settings
+ $ git config --list

D. Git Code Editor 
+ $ git config --global core.editor "Path of editor till exe"

E. Change Working directory
+ cd "Path pf folder"

# For Specific User
1. add File in local repository
+ $ touch <File Name>
Or 
+ $ echo "My Project" > <File Name>

2. Initialized the directory
+ $ git int

3. Clear the workspace
+ $ clear

4. Add individual file
+ $ git add <File name>

5. Add all the files
+ $ git add .

6. check the status of repository
+ $ git status

7. Remove file from local env
+ $ git rm --cached <File name>

8. add all the same extension file name
+ $ git add *.py 

9. commit the single file or changed file
+ $ git commit

10. commit all the added file 
+ $ git commit -m 'Comment about commit' 

11. If you want to ignore some of the files then use ".gitignore"
+ $ touch .gitignore
Add the file name & directory name into this file which you want to ignore while committing to main repository
  
12. Create branch of repository
+ $ git branch <BranchName>

13. To work on branch
+ $ git checkout <BranchName>

14. Merge the branch changes to Master repository
+ $ git merge <BranchName>

15. To work on GitHub remote repository
+ $ git remote
+ $ git remote add origin <GitHub Repository Path>

16. Push changes to GitHub remote repository
+ $ git push -u origin master

17. Copy the GitHub directory to local
+ $ git clone <GitHub Repository Path>

18. To Pull the data from GitHub remote repository
+ $ git pull

19. To Inspecting remote repository
+ $ git remote show origin

20. Fetching and Pulling from Your Remotes
+ $ git fetch <remote>

21. Showing Your Remotes
+ $ git remote -v

22. Renaming Remotes
+ $ git remote rename <Given Name> <New Name>

23. Removing Remotes
+ $ git remote remove <Remote Name>

24. Listing Tags
+ $ git tag
+ << $ git tag -l "Version">>

25. Annotate Tags
+ $ git tag -a <Version Name> -m "Modification Name"

26. Difference between two file [compression of two file]
+ $ git diff <file name>

27. Update existing git remote URL
+ $ git remote set-url origin new.git.url/here

28. How to update manually deleted files
+ $ git add -u
+ $ git commit -m "Manually deleted files"