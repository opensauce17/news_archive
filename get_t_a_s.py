#! /usr/bin/env python

import sqlite3
import json

con = sqlite3.connect("news/db/db.db")
cur = con.cursor()

title_sql_query = "SELECT x.title, COUNT(DISTINCT x.[title]) FROM (SELECT [title] FROM [au_news] UNION ALL SELECT [title] FROM [ca_news]\
UNION ALL SELECT [title] FROM [gb_news] UNION  SELECT [title] FROM [nz_news] UNION  SELECT [title] FROM [us_news]\
UNION  SELECT [title] FROM [za_news]) x GROUP BY x.title"
cur.execute(title_sql_query)
total_titles = (list(cur))
total_titles = len(total_titles)

author_sql_query = "SELECT x.author, COUNT(DISTINCT x.[author]) FROM (SELECT [author] FROM [au_news] UNION ALL SELECT [author] FROM [ca_news]\
UNION ALL SELECT [author] FROM [gb_news] UNION  SELECT [author] FROM [nz_news] UNION  SELECT [author] FROM [us_news]\
UNION  SELECT [author] FROM [za_news]) x GROUP BY x.author"

cur.execute(author_sql_query)
total_authors = (list(cur))
total_authors = len(total_authors)

sources_sql_query = "SELECT x.source, COUNT(DISTINCT x.[source]) FROM (SELECT [source] FROM [au_news] UNION ALL SELECT [source] FROM [ca_news]\
UNION ALL SELECT [source] FROM [gb_news] UNION  SELECT [source] FROM [nz_news] UNION  SELECT [source] FROM [us_news]\
UNION  SELECT [source] FROM [za_news]) x GROUP BY x.source"

cur.execute(sources_sql_query)
total_sources = (list(cur))
total_sources =  len(total_sources)

con.close()

totals = {
    "total_titles": total_titles,
    "total_authors": total_authors,
    "total_sources": total_sources
}

with open('news/analytics/tas.json', 'w') as f:
    json.dump(totals, f)