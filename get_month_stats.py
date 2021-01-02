#! /usr/bin/env python

import sqlite3
import json

def month_queries(query, month):

    con = sqlite3.connect("news/db/db.db")
    cur = con.cursor()
    r = cur.execute(query)
    total_titles = (list(r))
    total = len(total_titles)
    con.close()

    return total, month

aus = {
    "jan": "select * from au_news where '2021-01-01' <= publishedAt and publishedAt < '2021-02-01'",
    "feb": "select * from au_news where '2021-02-01' <= publishedAt and publishedAt < '2021-03-01'",
    "mar": "select * from au_news where '2021-03-01' <= publishedAt and publishedAt < '2021-04-01'",
    "apr": "select * from au_news where '2021-04-01' <= publishedAt and publishedAt < '2021-05-01'",
    "may": "select * from au_news where '2021-05-01' <= publishedAt and publishedAt < '2021-06-01'",
    "jun": "select * from au_news where '2021-06-01' <= publishedAt and publishedAt < '2021-07-01'",
    "jul": "select * from au_news where '2021-07-01' <= publishedAt and publishedAt < '2021-08-01'",
    "aug": "select * from au_news where '2021-08-01' <= publishedAt and publishedAt < '2021-09-01'",
    "sep": "select * from au_news where '2021-09-01' <= publishedAt and publishedAt < '2021-10-01'",
    "oct": "select * from au_news where '2021-10-01' <= publishedAt and publishedAt < '2021-11-01'",
    "nov": "select * from au_news where '2021-11-01' <= publishedAt and publishedAt < '2021-12-01'",
    "dec": "select * from au_news where '2021-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

can = {
    "jan": "select * from ca_news where '2021-01-01' <= publishedAt and publishedAt < '2021-02-01'",
    "feb": "select * from ca_news where '2021-02-01' <= publishedAt and publishedAt < '2021-03-01'",
    "mar": "select * from ca_news where '2021-03-01' <= publishedAt and publishedAt < '2021-04-01'",
    "apr": "select * from ca_news where '2021-04-01' <= publishedAt and publishedAt < '2021-05-01'",
    "may": "select * from ca_news where '2021-05-01' <= publishedAt and publishedAt < '2021-06-01'",
    "jun": "select * from ca_news where '2021-06-01' <= publishedAt and publishedAt < '2021-07-01'",
    "jul": "select * from ca_news where '2021-07-01' <= publishedAt and publishedAt < '2021-08-01'",
    "aug": "select * from ca_news where '2021-08-01' <= publishedAt and publishedAt < '2021-09-01'",
    "sep": "select * from ca_news where '2021-09-01' <= publishedAt and publishedAt < '2021-10-01'",
    "oct": "select * from ca_news where '2021-10-01' <= publishedAt and publishedAt < '2021-11-01'",
    "nov": "select * from ca_news where '2021-11-01' <= publishedAt and publishedAt < '2021-12-01'",
    "dec": "select * from ca_news where '2021-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

grb = {
    "jan": "select * from gb_news where '2021-01-01' <= publishedAt and publishedAt < '2021-02-01'",
    "feb": "select * from gb_news where '2021-02-01' <= publishedAt and publishedAt < '2021-03-01'",
    "mar": "select * from gb_news where '2021-03-01' <= publishedAt and publishedAt < '2021-04-01'",
    "apr": "select * from gb_news where '2021-04-01' <= publishedAt and publishedAt < '2021-05-01'",
    "may": "select * from gb_news where '2021-05-01' <= publishedAt and publishedAt < '2021-06-01'",
    "jun": "select * from gb_news where '2021-06-01' <= publishedAt and publishedAt < '2021-07-01'",
    "jul": "select * from gb_news where '2021-07-01' <= publishedAt and publishedAt < '2021-08-01'",
    "aug": "select * from gb_news where '2021-08-01' <= publishedAt and publishedAt < '2021-09-01'",
    "sep": "select * from gb_news where '2021-09-01' <= publishedAt and publishedAt < '2021-10-01'",
    "oct": "select * from gb_news where '2021-10-01' <= publishedAt and publishedAt < '2021-11-01'",
    "nov": "select * from gb_news where '2021-11-01' <= publishedAt and publishedAt < '2021-12-01'",
    "dec": "select * from gb_news where '2021-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

nzl = {
    "jan": "select * from nz_news where '2021-01-01' <= publishedAt and publishedAt < '2021-02-01'",
    "feb": "select * from nz_news where '2021-02-01' <= publishedAt and publishedAt < '2021-03-01'",
    "mar": "select * from nz_news where '2021-03-01' <= publishedAt and publishedAt < '2021-04-01'",
    "apr": "select * from nz_news where '2021-04-01' <= publishedAt and publishedAt < '2021-05-01'",
    "may": "select * from nz_news where '2021-05-01' <= publishedAt and publishedAt < '2021-06-01'",
    "jun": "select * from nz_news where '2021-06-01' <= publishedAt and publishedAt < '2021-07-01'",
    "jul": "select * from nz_news where '2021-07-01' <= publishedAt and publishedAt < '2021-08-01'",
    "aug": "select * from nz_news where '2021-08-01' <= publishedAt and publishedAt < '2021-09-01'",
    "sep": "select * from nz_news where '2021-09-01' <= publishedAt and publishedAt < '2021-10-01'",
    "oct": "select * from nz_news where '2021-10-01' <= publishedAt and publishedAt < '2021-11-01'",
    "nov": "select * from nz_news where '2021-11-01' <= publishedAt and publishedAt < '2021-12-01'",
    "dec": "select * from nz_news where '2021-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

usa = {
    "jan": "select * from us_news where '2021-01-01' <= publishedAt and publishedAt < '2021-02-01'",
    "feb": "select * from us_news where '2021-02-01' <= publishedAt and publishedAt < '2021-03-01'",
    "mar": "select * from us_news where '2021-03-01' <= publishedAt and publishedAt < '2021-04-01'",
    "apr": "select * from us_news where '2021-04-01' <= publishedAt and publishedAt < '2021-05-01'",
    "may": "select * from us_news where '2021-05-01' <= publishedAt and publishedAt < '2021-06-01'",
    "jun": "select * from us_news where '2021-06-01' <= publishedAt and publishedAt < '2021-07-01'",
    "jul": "select * from us_news where '2021-07-01' <= publishedAt and publishedAt < '2021-08-01'",
    "aug": "select * from us_news where '2021-08-01' <= publishedAt and publishedAt < '2021-09-01'",
    "sep": "select * from us_news where '2021-09-01' <= publishedAt and publishedAt < '2021-10-01'",
    "oct": "select * from us_news where '2021-10-01' <= publishedAt and publishedAt < '2021-11-01'",
    "nov": "select * from us_news where '2021-11-01' <= publishedAt and publishedAt < '2021-12-01'",
    "dec": "select * from us_news where '2021-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

saf = {
    "jan": "select * from za_news where '2021-01-01' <= publishedAt and publishedAt < '2021-02-01'",
    "feb": "select * from za_news where '2021-02-01' <= publishedAt and publishedAt < '2021-03-01'",
    "mar": "select * from za_news where '2021-03-01' <= publishedAt and publishedAt < '2021-04-01'",
    "apr": "select * from za_news where '2021-04-01' <= publishedAt and publishedAt < '2021-05-01'",
    "may": "select * from za_news where '2021-05-01' <= publishedAt and publishedAt < '2021-06-01'",
    "jun": "select * from za_news where '2021-06-01' <= publishedAt and publishedAt < '2021-07-01'",
    "jul": "select * from za_news where '2021-07-01' <= publishedAt and publishedAt < '2021-08-01'",
    "aug": "select * from za_news where '2021-08-01' <= publishedAt and publishedAt < '2021-09-01'",
    "sep": "select * from za_news where '2021-09-01' <= publishedAt and publishedAt < '2021-10-01'",
    "oct": "select * from za_news where '2021-10-01' <= publishedAt and publishedAt < '2021-11-01'",
    "nov": "select * from za_news where '2021-11-01' <= publishedAt and publishedAt < '2021-12-01'",
    "dec": "select * from za_news where '2021-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

au = {}
ca = {}
gb = {}
nz = {}
us = {}
za = {}

for k,v in aus.items():
    total, month = month_queries(v, k)
    au[month] = total

for k,v in can.items():
    total, month = month_queries(v, k)
    ca[month] = total

for k,v in grb.items():
    total, month = month_queries(v, k)
    gb[month] = total

for k,v in nzl.items():
    total, month = month_queries(v, k)
    nz[month] = total

for k,v in usa.items():
    total, month = month_queries(v, k)
    us[month] = total

for k,v in saf.items():
    total, month = month_queries(v, k)
    za[month] = total

january = []
february = []
march = []
april = []
may = []
june = []
july = []
august = []
september = []
october = []
november = []
december = []

for k,v in au.items():
    if k == 'jan':
        january.append(v)
    if k == 'feb':
        february.append(v)
    if k == 'mar':
        march.append(v)
    if k == 'apr':
        april.append(v)
    if k == 'may':
        may.append(v)
    if k == 'jun':
        june.append(v)
    if k == 'jul':
        july.append(v)
    if k == 'aug':
        august.append(v)
    if k == 'sep':
        september.append(v)
    if k == 'oct':
        october.append(v)
    if k == 'nov':
        november.append(v)
    if k == 'dec':
        december.append(v)

for k,v in ca.items():
    if k == 'jan':
        january.append(v)
    if k == 'feb':
        february.append(v)
    if k == 'mar':
        march.append(v)
    if k == 'apr':
        april.append(v)
    if k == 'may':
        may.append(v)
    if k == 'jun':
        june.append(v)
    if k == 'jul':
        july.append(v)
    if k == 'aug':
        august.append(v)
    if k == 'sep':
        september.append(v)
    if k == 'oct':
        october.append(v)
    if k == 'nov':
        november.append(v)
    if k == 'dec':
        december.append(v)

for k,v in gb.items():
    if k == 'jan':
        january.append(v)
    if k == 'feb':
        february.append(v)
    if k == 'mar':
        march.append(v)
    if k == 'apr':
        april.append(v)
    if k == 'may':
        may.append(v)
    if k == 'jun':
        june.append(v)
    if k == 'jul':
        july.append(v)
    if k == 'aug':
        august.append(v)
    if k == 'sep':
        september.append(v)
    if k == 'oct':
        october.append(v)
    if k == 'nov':
        november.append(v)
    if k == 'dec':
        december.append(v)

for k,v in nz.items():
    if k == 'jan':
        january.append(v)
    if k == 'feb':
        february.append(v)
    if k == 'mar':
        march.append(v)
    if k == 'apr':
        april.append(v)
    if k == 'may':
        may.append(v)
    if k == 'jun':
        june.append(v)
    if k == 'jul':
        july.append(v)
    if k == 'aug':
        august.append(v)
    if k == 'sep':
        september.append(v)
    if k == 'oct':
        october.append(v)
    if k == 'nov':
        november.append(v)
    if k == 'dec':
        december.append(v)

for k,v in us.items():
    if k == 'jan':
        january.append(v)
    if k == 'feb':
        february.append(v)
    if k == 'mar':
        march.append(v)
    if k == 'apr':
        april.append(v)
    if k == 'may':
        may.append(v)
    if k == 'jun':
        june.append(v)
    if k == 'jul':
        july.append(v)
    if k == 'aug':
        august.append(v)
    if k == 'sep':
        september.append(v)
    if k == 'oct':
        october.append(v)
    if k == 'nov':
        november.append(v)
    if k == 'dec':
        december.append(v)

for k,v in za.items():
    if k == 'jan':
        january.append(v)
    if k == 'feb':
        february.append(v)
    if k == 'mar':
        march.append(v)
    if k == 'apr':
        april.append(v)
    if k == 'may':
        may.append(v)
    if k == 'jun':
        june.append(v)
    if k == 'jul':
        july.append(v)
    if k == 'aug':
        august.append(v)
    if k == 'sep':
        september.append(v)
    if k == 'oct':
        october.append(v)
    if k == 'nov':
        november.append(v)
    if k == 'dec':
        december.append(v)


january = sum(january)
february = sum(february)
march = sum(march)
april = sum(april)
may = sum(may)
june = sum(june)
july = sum(july)
august = sum(august)
september = sum(september)
october = sum(october)
november = sum(november)
december = sum(december)

news_per_month_2021 = {
    "january": january,
    "february": february,
    "march": march,
    "april": april,
    "may": may,
    "june": june,
    "july": july,
    "august": august,
    "september": september,
    "october": october,
    "november": november,
    "december": december
}

with open('news/analytics/per_month.json', 'w') as f:
    json.dump(news_per_month_2021, f)