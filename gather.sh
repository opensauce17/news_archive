#!/bin/bash

gather/au_news.py
gather/ca_news.py
gather/nz_news.py
gather/gb_news.py
gather/us_news.py
gather/za_news.py

message="auto-commit from $USER@$(hostname -s) on $(date)"
GIT=`which git`
#REPO_DIR=~/org
#cd ${REPO_DIR}
${GIT} add --all .
${GIT} commit -m "$message"

gitPush=$(${GIT} push -vvv git@github.com:opensauce17/news_archive.git master 2>&1)
echo "$gitPush"
