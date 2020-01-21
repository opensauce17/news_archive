#!/bin/bash

/opt/news_archive/gather/au_news.py
/opt/news_archive/gather/ca_news.py
/opt/news_archive/gather/nz_news.py
/opt/news_archive/gather/gb_news.py
/opt/news_archive/gather/us_news.py
/opt/news_archive/gather/za_news.py

message="auto-commit from Mike Hyland  on $(date)"
GIT=`which git`
REPO_DIR=/opt/news_archive
cd ${REPO_DIR}
${GIT} config user.email "opensauce17@gmail.com"
${GIT} config user.name "Mike Hyland"
${GIT} add --all .
${GIT} commit -m "$message"
${GIT} checkout master
${GIT} merge deploy
${GIT} merge push
${GIT} checkout deploy

gitPush=$(${GIT} push -vvv git@github.com:opensauce17/news_archive.git master 2>&1)
echo "$gitPush"
