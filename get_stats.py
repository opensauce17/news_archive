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
    "jan": "select * from au_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'",
    "feb": "select * from au_news where '2020-02-01' <= publishedAt and publishedAt < '2020-03-01'",
    "mar": "select * from au_news where '2020-03-01' <= publishedAt and publishedAt < '2020-04-01'",
    "apr": "select * from au_news where '2020-04-01' <= publishedAt and publishedAt < '2020-05-01'",
    "may": "select * from au_news where '2020-05-01' <= publishedAt and publishedAt < '2020-06-01'",
    "jun": "select * from au_news where '2020-06-01' <= publishedAt and publishedAt < '2020-07-01'",
    "jul": "select * from au_news where '2020-07-01' <= publishedAt and publishedAt < '2020-08-01'",
    "aug": "select * from au_news where '2020-08-01' <= publishedAt and publishedAt < '2020-09-01'",
    "sep": "select * from au_news where '2020-09-01' <= publishedAt and publishedAt < '2020-10-01'",
    "oct": "select * from au_news where '2020-10-01' <= publishedAt and publishedAt < '2020-11-01'",
    "nov": "select * from au_news where '2020-11-01' <= publishedAt and publishedAt < '2020-12-01'",
    "dec": "select * from au_news where '2020-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

can = {
    "jan": "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'",
    "feb": "select * from ca_news where '2020-02-01' <= publishedAt and publishedAt < '2020-03-01'",
    "mar": "select * from ca_news where '2020-03-01' <= publishedAt and publishedAt < '2020-04-01'",
    "apr": "select * from ca_news where '2020-04-01' <= publishedAt and publishedAt < '2020-05-01'",
    "may": "select * from ca_news where '2020-05-01' <= publishedAt and publishedAt < '2020-06-01'",
    "jun": "select * from ca_news where '2020-06-01' <= publishedAt and publishedAt < '2020-07-01'",
    "jul": "select * from ca_news where '2020-07-01' <= publishedAt and publishedAt < '2020-08-01'",
    "aug": "select * from ca_news where '2020-08-01' <= publishedAt and publishedAt < '2020-09-01'",
    "sep": "select * from ca_news where '2020-09-01' <= publishedAt and publishedAt < '2020-10-01'",
    "oct": "select * from ca_news where '2020-10-01' <= publishedAt and publishedAt < '2020-11-01'",
    "nov": "select * from ca_news where '2020-11-01' <= publishedAt and publishedAt < '2020-12-01'",
    "dec": "select * from ca_news where '2020-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

grb = {
    "jan": "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'",
    "feb": "select * from gb_news where '2020-02-01' <= publishedAt and publishedAt < '2020-03-01'",
    "mar": "select * from gb_news where '2020-03-01' <= publishedAt and publishedAt < '2020-04-01'",
    "apr": "select * from gb_news where '2020-04-01' <= publishedAt and publishedAt < '2020-05-01'",
    "may": "select * from gb_news where '2020-05-01' <= publishedAt and publishedAt < '2020-06-01'",
    "jun": "select * from gb_news where '2020-06-01' <= publishedAt and publishedAt < '2020-07-01'",
    "jul": "select * from gb_news where '2020-07-01' <= publishedAt and publishedAt < '2020-08-01'",
    "aug": "select * from gb_news where '2020-08-01' <= publishedAt and publishedAt < '2020-09-01'",
    "sep": "select * from gb_news where '2020-09-01' <= publishedAt and publishedAt < '2020-10-01'",
    "oct": "select * from gb_news where '2020-10-01' <= publishedAt and publishedAt < '2020-11-01'",
    "nov": "select * from gb_news where '2020-11-01' <= publishedAt and publishedAt < '2020-12-01'",
    "dec": "select * from gb_news where '2020-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

nzl = {
    "jan": "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'",
    "feb": "select * from nz_news where '2020-02-01' <= publishedAt and publishedAt < '2020-03-01'",
    "mar": "select * from nz_news where '2020-03-01' <= publishedAt and publishedAt < '2020-04-01'",
    "apr": "select * from nz_news where '2020-04-01' <= publishedAt and publishedAt < '2020-05-01'",
    "may": "select * from nz_news where '2020-05-01' <= publishedAt and publishedAt < '2020-06-01'",
    "jun": "select * from nz_news where '2020-06-01' <= publishedAt and publishedAt < '2020-07-01'",
    "jul": "select * from nz_news where '2020-07-01' <= publishedAt and publishedAt < '2020-08-01'",
    "aug": "select * from nz_news where '2020-08-01' <= publishedAt and publishedAt < '2020-09-01'",
    "sep": "select * from nz_news where '2020-09-01' <= publishedAt and publishedAt < '2020-10-01'",
    "oct": "select * from nz_news where '2020-10-01' <= publishedAt and publishedAt < '2020-11-01'",
    "nov": "select * from nz_news where '2020-11-01' <= publishedAt and publishedAt < '2020-12-01'",
    "dec": "select * from nz_news where '2020-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

usa = {
    "jan": "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'",
    "feb": "select * from us_news where '2020-02-01' <= publishedAt and publishedAt < '2020-03-01'",
    "mar": "select * from us_news where '2020-03-01' <= publishedAt and publishedAt < '2020-04-01'",
    "apr": "select * from us_news where '2020-04-01' <= publishedAt and publishedAt < '2020-05-01'",
    "may": "select * from us_news where '2020-05-01' <= publishedAt and publishedAt < '2020-06-01'",
    "jun": "select * from us_news where '2020-06-01' <= publishedAt and publishedAt < '2020-07-01'",
    "jul": "select * from us_news where '2020-07-01' <= publishedAt and publishedAt < '2020-08-01'",
    "aug": "select * from us_news where '2020-08-01' <= publishedAt and publishedAt < '2020-09-01'",
    "sep": "select * from us_news where '2020-09-01' <= publishedAt and publishedAt < '2020-10-01'",
    "oct": "select * from us_news where '2020-10-01' <= publishedAt and publishedAt < '2020-11-01'",
    "nov": "select * from us_news where '2020-11-01' <= publishedAt and publishedAt < '2020-12-01'",
    "dec": "select * from us_news where '2020-12-01' <= publishedAt and publishedAt < '2021-01-01'"
}

saf = {
    "jan": "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'",
    "feb": "select * from za_news where '2020-02-01' <= publishedAt and publishedAt < '2020-03-01'",
    "mar": "select * from za_news where '2020-03-01' <= publishedAt and publishedAt < '2020-04-01'",
    "apr": "select * from za_news where '2020-04-01' <= publishedAt and publishedAt < '2020-05-01'",
    "may": "select * from za_news where '2020-05-01' <= publishedAt and publishedAt < '2020-06-01'",
    "jun": "select * from za_news where '2020-06-01' <= publishedAt and publishedAt < '2020-07-01'",
    "jul": "select * from za_news where '2020-07-01' <= publishedAt and publishedAt < '2020-08-01'",
    "aug": "select * from za_news where '2020-08-01' <= publishedAt and publishedAt < '2020-09-01'",
    "sep": "select * from za_news where '2020-09-01' <= publishedAt and publishedAt < '2020-10-01'",
    "oct": "select * from za_news where '2020-10-01' <= publishedAt and publishedAt < '2020-11-01'",
    "nov": "select * from za_news where '2020-11-01' <= publishedAt and publishedAt < '2020-12-01'",
    "dec": "select * from za_news where '2020-12-01' <= publishedAt and publishedAt < '2021-01-01'"
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

# total = january + february + march + april + may + june + july + august + september + october + november + december

# print(total)

news_per_month_2020 = {
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

with open('per_month.json', 'w') as f:
    json.dump(news_per_month_2020, f)


# print(january)
# print(february)
# print(march)
# print(april)
# print(may)
# print(june)
# print(july)
# print(august)
# print(september)
# print(october)
# print(november)
# print(december)


# print('Australia:')
# print(au)
# print('Canada:')
# print(ca)
# print('Great Britain:')
# print(gb)
# print('New Zealand:')
# print(nz)
# print('United States:')
# print(us)
# print('South Africa:')
# print(za)
    

#total = queries(date_au_feb_sql_query, 'january', 'au')








#AU
# date_au_jan_sql_query = "select * from au_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_au_feb_sql_query = "select * from au_news where '2020-02-01' <= publishedAt and publishedAt < '2020-03-01'"
# date_au_mar_sql_query = "select * from au_news where '2020-03-01' <= publishedAt and publishedAt < '2020-04-01'"
# date_au_apr_sql_query = "select * from au_news where '2020-04-01' <= publishedAt and publishedAt < '2020-05-01'"
# date_au_may_sql_query = "select * from au_news where '2020-05-01' <= publishedAt and publishedAt < '2020-06-01'"
# date_au_jun_sql_query = "select * from au_news where '2020-06-01' <= publishedAt and publishedAt < '2020-07-01'"
# date_au_jul_sql_query = "select * from au_news where '2020-07-01' <= publishedAt and publishedAt < '2020-08-01'"
# date_au_aug_sql_query = "select * from au_news where '2020-08-01' <= publishedAt and publishedAt < '2020-09-01'"
# date_au_sep_sql_query = "select * from au_news where '2020-09-01' <= publishedAt and publishedAt < '2020-10-01'"
# date_au_oct_sql_query = "select * from au_news where '2020-10-01' <= publishedAt and publishedAt < '2020-11-01'"
# date_au_nov_sql_query = "select * from au_news where '2020-11-01' <= publishedAt and publishedAt < '2020-12-01'"
# date_au_dec_sql_query = "select * from au_news where '2020-12-01' <= publishedAt and publishedAt < '2021-01-01'"

# jan = cur.execute(date_au_jan_sql_query)
# feb = cur.execute(date_au_feb_sql_query)
# mar = cur.execute(date_au_mar_sql_query)
# apr = cur.execute(date_au_apr_sql_query)
# may = cur.execute(date_au_may_sql_query)
# jun = cur.execute(date_au_jun_sql_query)
# jul = cur.execute(date_au_jul_sql_query)
# aug = cur.execute(date_au_aug_sql_query)
# sep = cur.execute(date_au_sep_sql_query)
# octo = cur.execute(date_au_oct_sql_query)
# nov = cur.execute(date_au_nov_sql_query)
# dec = cur.execute(date_au_dec_sql_query)

# total_au_jan_titles = (list(jan))
# total_au_feb_titles = (list(feb))
# total_au_mar_titles = (list(mar))
# total_au_apr_titles = (list(apr))
# total_au_may_titles = (list(may))
# total_au_jun_titles = (list(jun))
# total_au_jul_titles = (list(jul))
# total_au_aug_titles = (list(aug))
# total_au_sep_titles = (list(sep))
# total_au_octo_titles = (list(octo))
# total_au_nov_titles = (list(nov))
# total_au_dec_titles = (list(dec))

# print len(total_au_jan_titles)
#print len(total_au_feb_titles)
# print len(total_au_mar_titles)
# print len(total_au_apr_titles)
# print len(total_au_may_titles)
# print len(total_au_jun_titles)
# print len(total_au_jul_titles)
# print len(total_au_aug_titles)
# print len(total_au_sep_titles)
# print len(total_au_octo_titles)
# print len(total_au_nov_titles)
# print len(total_au_dec_titles)

# #CA
# date_ca_jan_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_feb_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_mar_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_apr_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_may_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_jun_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_jul_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_aug_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_sep_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_oct_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_nov_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_ca_dec_sql_query = "select * from ca_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"

# cur.execute(date_sql_query)
# total_titles = (list(cur))
# print(total_titles)

# #GB
# date_gb_jan_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_feb_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_mar_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_apr_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_may_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_jun_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_jul_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_aug_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_sep_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_oct_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_nov_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_gb_dec_sql_query = "select * from gb_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"

# cur.execute(date_sql_query)
# total_titles = (list(cur))
# print(total_titles)

# #NZ
# date_nz_jan_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_feb_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_mar_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_apr_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_may_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_jun_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_jul_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_aug_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_sep_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_oct_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_nov_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_nz_dec_sql_query = "select * from nz_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"

# cur.execute(date_sql_query)
# total_titles = (list(cur))
# print(total_titles)

# #US
# date_us_jan_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_feb_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_mar_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_apr_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_may_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_jun_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_jul_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_aug_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_sep_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_oct_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_nov_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_us_dec_sql_query = "select * from us_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"

# cur.execute(date_sql_query)
# total_titles = (list(cur))
# print(total_titles)

# #ZA
# date_za_jan_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_feb_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_mar_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_apr_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_may_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_jun_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_jul_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_aug_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_sep_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_oct_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_nov_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"
# date_za_dec_sql_query = "select * from za_news where '2020-01-01' <= publishedAt and publishedAt < '2020-02-01'"

# cur.execute(date_sql_query)
# total_titles = (list(cur))
# print(total_titles)


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

# sources_sql_query = "SELECT x.source, COUNT(DISTINCT x.[source]) FROM (SELECT [source] FROM [au_news] UNION ALL SELECT [source] FROM [ca_news]\
#  UNION ALL SELECT [source] FROM [gb_news] UNION  SELECT [source] FROM [nz_news] UNION  SELECT [source] FROM [us_news]\
#  UNION  SELECT [source] FROM [za_news]) x GROUP BY x.source"

# cur.execute(sources_sql_query)
# total_sources = (list(cur))
# print(total_sources)
# total_sources = list(dict.fromkeys(total_sources))
# print len(total_sources)

