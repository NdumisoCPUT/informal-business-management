#!/bin/bash

# 1. Get input for branch name and commit message
read -p "Enter branch name (e.g. ndumiso-cput-feature-x): " branch
read -p "Enter commit message: " message

# 2. Create branch and switch to it
git checkout -b "$branch"

# 3. Stage and commit changes
git add .
git commit -m "$message"

# 4. Push to origin
git push -u origin "$branch"

# 5. Open browser to GitHub PR page
remote_url=$(git config --get remote.origin.url | sed 's/.git$//')
repo_name=$(basename -s .git `git config --get remote.origin.url`)
user_name=$(basename `git config --get remote.origin.url | cut -d':' -f2 | cut -d'/' -f1`)
xdg-open "https://github.com/$user_name/$repo_name/compare/main...$branch?expand=1"
