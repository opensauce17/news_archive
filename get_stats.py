#! /usr/bin/env python

import sqlite3

con = sqlite3.connect("news/db/db.db")

cur = con.cursor()

# title_sql_query = "SELECT x.title, COUNT(DISTINCT x.[title]) FROM (SELECT [title] FROM [au_news] UNION ALL SELECT [title] FROM [ca_news]\
#  UNION ALL SELECT [title] FROM [gb_news] UNION  SELECT [title] FROM [nz_news] UNION  SELECT [title] FROM [us_news]\
#  UNION  SELECT [title] FROM [za_news]) x GROUP BY x.title"
# cur.execute(title_sql_query)
# total_titles = (list(cur))
# total_titles = list(dict.fromkeys(total_titles))
# print len(total_titles)

# author_sql_query = "SELECT x.author, COUNT(DISTINCT x.[author]) FROM (SELECT [author] FROM [au_news] UNION ALL SELECT [author] FROM [ca_news]\
#  UNION ALL SELECT [author] FROM [gb_news] UNION  SELECT [author] FROM [nz_news] UNION  SELECT [author] FROM [us_news]\
#  UNION  SELECT [author] FROM [za_news]) x GROUP BY x.author"

# cur.execute(author_sql_query)
# total_authors = (list(cur))
# total_authors = list(dict.fromkeys(total_authors))
# print(total_authors)
# # print len(total_authors)

sources_sql_query = "SELECT x.source, COUNT(DISTINCT x.[source]) FROM (SELECT [source] FROM [au_news] UNION ALL SELECT [source] FROM [ca_news]\
 UNION ALL SELECT [source] FROM [gb_news] UNION  SELECT [source] FROM [nz_news] UNION  SELECT [source] FROM [us_news]\
 UNION  SELECT [source] FROM [za_news]) x GROUP BY x.source"

cur.execute(sources_sql_query)
total_sources = (list(cur))
print(total_sources)
# total_sources = list(dict.fromkeys(total_sources))
# print len(total_sources)

con.close()