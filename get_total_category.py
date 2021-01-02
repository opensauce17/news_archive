#! /usr/bin/env python

import sqlite3
import json

def type_queries(query, news_type):

    con = sqlite3.connect("news/db/db.db")
    cur = con.cursor()
    r = cur.execute(query)
    total_titles = (list(r))
    total = len(total_titles)
    con.close()

    return total, news_type

aus = {
    "headlines": "select * from au_news where news_type = 'headlines' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "business": "select * from au_news where news_type = 'business' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "technology": "select * from au_news where news_type = 'technology' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "health": "select * from au_news where news_type = 'health' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "science": "select * from au_news where news_type = 'science' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "sport": "select * from au_news where news_type = 'sports' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "entertainment": "select * from au_news where news_type = 'entertainment' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'"
}

can = {
    "headlines": "select * from ca_news where news_type = 'headlines' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "business": "select * from ca_news where news_type = 'business' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "technology": "select * from ca_news where news_type = 'technology' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "health": "select * from ca_news where news_type = 'health' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "science": "select * from ca_news where news_type = 'science' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "sport": "select * from ca_news where news_type = 'sports' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "entertainment": "select * from ca_news where news_type = 'entertainment' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'"
}

grb = {
    "headlines": "select * from gb_news where news_type = 'headlines' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "business": "select * from gb_news where news_type = 'business' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "technology": "select * from gb_news where news_type = 'technology' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "health": "select * from gb_news where news_type = 'health' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "science": "select * from gb_news where news_type = 'science' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "sport": "select * from gb_news where news_type = 'sports' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "entertainment": "select * from gb_news where news_type = 'entertainment' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'"
}

nzl = {
    "headlines": "select * from nz_news where news_type = 'headlines' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "business": "select * from nz_news where news_type = 'business' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "technology": "select * from nz_news where news_type = 'technology' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "health": "select * from nz_news where news_type = 'health' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "science": "select * from nz_news where news_type = 'science' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "sport": "select * from nz_news where news_type = 'sports' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "entertainment": "select * from nz_news where news_type = 'entertainment' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'"
}

usa = {
    "headlines": "select * from us_news where news_type = 'headlines' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "business": "select * from us_news where news_type = 'business' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "technology": "select * from us_news where news_type = 'technology' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "health": "select * from us_news where news_type = 'health' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "science": "select * from us_news where news_type = 'science' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "sport": "select * from us_news where news_type = 'sports' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "entertainment": "select * from us_news where news_type = 'entertainment' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'"
}

saf = {
    "headlines": "select * from za_news where news_type = 'headlines' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "business": "select * from za_news where news_type = 'business' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "technology": "select * from za_news where news_type = 'technology' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "health": "select * from za_news where news_type = 'health' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "science": "select * from za_news where news_type = 'science' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "sport": "select * from za_news where news_type = 'sports' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'",
    "entertainment": "select * from za_news where news_type = 'entertainment' and '2021-01-01' <= publishedAt and publishedAt < '2021-12-31'"
}

au = {}
ca = {}
gb = {}
nz = {}
us = {}
za = {}

for k,v in aus.items():
    total, news_type = type_queries(v,k)
    au[news_type] = total

for k,v in can.items():
    total, news_type = type_queries(v,k)
    ca[news_type] = total

for k,v in grb.items():
    total, news_type = type_queries(v,k)
    gb[news_type] = total

for k,v in nzl.items():
    total, news_type = type_queries(v,k)
    nz[news_type] = total

for k,v in usa.items():
    total, news_type = type_queries(v,k)
    us[news_type] = total

for k,v in saf.items():
    total, news_type = type_queries(v,k)
    za[news_type] = total

headlines = []
business = []
technology = []
health = []
science = []
sport = []
entertainment = []

# AU

for k,v in au.items():
    if k == 'headlines':
        headlines.append(v)
    if k == 'business':
        business.append(v)
    if k == 'technology':
        technology.append(v)
    if k == 'health':
        health.append(v)
    if k == 'science':
        science.append(v)
    if k == 'sport':
        sport.append(v)
    if k == 'entertainment':
        entertainment.append(v)

# CA

for k,v in ca.items():
    if k == 'headlines':
        headlines.append(v)
    if k == 'business':
        business.append(v)
    if k == 'technology':
        technology.append(v)
    if k == 'health':
        health.append(v)
    if k == 'science':
        science.append(v)
    if k == 'sport':
        sport.append(v)
    if k == 'entertainment':
        entertainment.append(v)

# GB

for k,v in gb.items():
    if k == 'headlines':
        headlines.append(v)
    if k == 'business':
        business.append(v)
    if k == 'technology':
        technology.append(v)
    if k == 'health':
        health.append(v)
    if k == 'science':
        science.append(v)
    if k == 'sport':
        sport.append(v)
    if k == 'entertainment':
        entertainment.append(v)

# NZ

for k,v in nz.items():
    if k == 'headlines':
        headlines.append(v)
    if k == 'business':
        business.append(v)
    if k == 'technology':
        technology.append(v)
    if k == 'health':
        health.append(v)
    if k == 'science':
        science.append(v)
    if k == 'sport':
        sport.append(v)
    if k == 'entertainment':
        entertainment.append(v)

# US

for k,v in us.items():
    if k == 'headlines':
        headlines.append(v)
    if k == 'business':
        business.append(v)
    if k == 'technology':
        technology.append(v)
    if k == 'health':
        health.append(v)
    if k == 'science':
        science.append(v)
    if k == 'sport':
        sport.append(v)
    if k == 'entertainment':
        entertainment.append(v)

# ZA

for k,v in za.items():
    if k == 'headlines':
        headlines.append(v)
    if k == 'business':
        business.append(v)
    if k == 'technology':
        technology.append(v)
    if k == 'health':
        health.append(v)
    if k == 'science':
        science.append(v)
    if k == 'sport':
        sport.append(v)
    if k == 'entertainment':
        entertainment.append(v)

total_headlines = sum(headlines)
total_business = sum(business)
total_technology = sum(technology)
total_health = sum(health)
total_science = sum(science)
total_sport = sum(sport)
total_entertainment = sum(entertainment)

total_title_per_category = {
    'headlines': total_headlines,
    'business': total_business,
    'technology': total_technology,
    'health': total_health,
    'science': total_science,
    'sport': total_sport,
    'entertainment': total_entertainment
}

with open('news/analytics/title_per_category.json', 'w') as f:
    json.dump(total_title_per_category, f)