#! /usr/bin/env python

from datetime import datetime, date, timedelta
from sqlalchemy import and_
import sqlite3

conn = sqlite3.connect('/Users/michael.hyland/python_prod/news_archive/news/db/db.db')
cur = conn.cursor()

from_date = "2020-06-01"
to_date = "2020-06-30"

f_from_date = datetime.strptime(from_date, "%Y-%m-%d")
f_from_full_date = f_from_date.strftime("%d %B, %Y")


f_to_date = datetime.strptime(to_date, "%Y-%m-%d")
f_to_full_date = f_to_date.strftime("%d %B, %Y")

f_year = from_date.split('-')[0]
f_month = from_date.split('-')[1]
f_day = from_date.split('-')[2]

t_year = to_date.split('-')[0]
t_month = to_date.split('-')[1]
t_day = to_date.split('-')[2]

d1 = date(int(f_year), int(f_month), int(f_day))
d2 = date(int(t_year), int(t_month), int(t_day))

dd = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]

d = "'%2020-01-20%'"
sqlite_select_query = "SELECT description FROM au_news WHERE publishedAt LIKE {}".format(d)
#print(sqlite_select_query)

cur.execute(sqlite_select_query)

rows = cur.fetchall()

words = []

try:
    for row in rows:
        l = (list(row))
        for i in l:
            words.append(i)
        #s = ' '.join(l)
        #print(s)
except TypeError:
    pass

print(words)
#print(rows)

""" for d in dd:
    #d = f"'%{d}%'"
    d = "'%2020-01-20%'"
    sqlite_select_query = "SELECT description FROM au_news WHERE publishedAt LIKE {}".format(d)
    print(sqlite_select_query) """
"""     cur.execute(sqlite_select_query)

    rows = cur.fetchall()

    print(rows)
    wait(10) """

"""     headlines = []

    for row in rows:
        headlines.append(row)

    print(headlines)
         """


