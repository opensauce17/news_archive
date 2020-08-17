#! /usr/bin/env python

import sqlite3
import json

def sql_query(country, table):

    con = sqlite3.connect("news/db/db.db")
    cur = con.cursor()

    title_sql_query = "SELECT title FROM {}".format(table)
    cur.execute(title_sql_query)
    total_titles = (list(cur))
    total_titles = len(total_titles)
    country = country
    con.close()

    return total_titles, country

tables = {
    'au': 'au_news',
    'ca': 'ca_news',
    'gb': 'gb_news',
    'nz': 'nz_news',
    'us': 'us_news',
    'za': 'za_news'
}

country_totals = {}

for k,v in tables.items():
    total, country = sql_query(k,v)
    country_totals[country] = total

with open('news/analytics/country_totals.json', 'w') as f:
    json.dump(country_totals, f)
