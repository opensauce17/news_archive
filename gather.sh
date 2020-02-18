#!/bin/bash

/opt/news_archive/gather/au_news.py
/opt/news_archive/gather/ca_news.py
/opt/news_archive/gather/nz_news.py
/opt/news_archive/gather/gb_news.py
/opt/news_archive/gather/us_news.py
/opt/news_archive/gather/za_news.py

/usr/local/bin/aws s3 rm s3://newsarchive-db-backup/db.db

/usr/local/bin/aws  s3 cp /opt/news_archive/news/db/db.db s3://newsarchive-db-backup
