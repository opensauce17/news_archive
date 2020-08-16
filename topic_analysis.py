#! /usr/bin/env python
from PyDictionary import PyDictionary
import collections
from datetime import datetime, date, timedelta
from sqlalchemy import and_
import sqlite3
import json

dictionary=PyDictionary()
conn = sqlite3.connect('news/db/db.db')
cur = conn.cursor()

today = datetime.today().strftime('%Y-%m-%d')

from_date = "2020-01-01"
to_date = today

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

t_list = []

for d in dd:
    d = f"'%{d}%'"
    #d = "'%2020-01-20%'"
    sqlite_select_query = "SELECT description, content, title FROM au_news WHERE publishedAt LIKE {}  \
        UNION \
             SELECT description, content, title FROM ca_news WHERE publishedAt LIKE {} \
        UNION \
             SELECT description, content, title FROM gb_news WHERE publishedAt LIKE {} \
        UNION \
             SELECT description, content, title FROM nz_news WHERE publishedAt LIKE {} \
        UNION \
             SELECT description, content, title FROM za_news WHERE publishedAt LIKE {} \
        UNION \
             SELECT description, content, title FROM us_news WHERE publishedAt LIKE {}".format(d, d, d, d, d, d)
    #sqlite_select_query = "SELECT description, content, title FROM nz_news WHERE publishedAt LIKE {} AND news_type = 'sports'".format(d)

    cur.execute(sqlite_select_query)

    rows = cur.fetchall()

    words = []

    try:
        for row in rows:
            l = (list(row))
            for i in l:
                words.append(i)

    except TypeError:
        pass

    word_list = []

    for i in words:
        try:
            for word in i.split():
                w = word.replace(".", "").replace(",", "")
                #print(w)
                word_list.append(w)
        except AttributeError:
            pass


    collection = [item for item, count in collections.Counter(word_list).items() if count > 200]

    remove_words = ['and', 'the', 'for', 'are', 'at', 'The', 'is', 'a', 'on', 'was', 'it', 'an', 'in',
     'of', 'but', 'be', 'he', 'she', 'A', 'up', 'can', 'at', 'by', 'can', 'now', 'his', 'for', 'his',
     'her', 'hers', 'all', 'you', 'that', 'their', 'not', 'this', 'will', 'new', 'as', 'have', 'from',
     'with', 'been', 'more', 'after', 'which', 'has', 'to', 'its', 'people', 'one', 'over', 'about',
     'just', 'some', 'who', 'could', 'said', 'out', 'they', 'or', 'may', 'your', 'during', 'than', 'had',
    'first', 'into', '-', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
    'years', 'game', 'study', 'says', 'In', 'in', 'were', 'how', 'time', 'we', 'when', 'our',
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'I', 'what', 'coming',
    'found', 'Some', 'some', 'know', 'week', 'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December', 'many', 'if', 'like', 'them',
    'most', 'get', 'between', 'best', 'even', 'would', 'do', 'This', 'But', 'but', 'should', 'also',
    'see', 'back', 'It', 'All', 'News', 'Australia', 'Australian', 'NEWScomau', 'chars]', '2020', '2019',
    'say', 'no', 'On', 'there', 'off', 'Is' ,'As', 'so', "it's", 'To', 'any', 'news', 'while', 'other', 'take',
    '--', 'announced' ,'look', 'last', 'man', '…', 'against', 'according', '—', '|', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '10', '/', 'One', 'You', 'year', 'day', 'make', 'way', 'By', 'ago', 'With', '–',
    'For', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'From', 'down', 'free', 'home', 'latest',
    'South', 'Africa', 'season', 'World', 'New Zealand', 'Canada', 'Zealand', 'company', 'long', 'around',
    'next', 'While', 'need', 'before', 'might', 'came', 'soon', 'took', 'being', 'today', 'since', 'only',
    'After', 'set', 'Stuffconz', 'Herald']
    
    new_collection = [word for word in collection if word not in remove_words]

    for i in new_collection:
        # print(i)
        t_list.append(i)


def most_frequent(List): 
    return max(set(List), key = List.count)

#print(most_frequent(t_list))

most_common = {
    'most_common': (most_frequent(t_list))
}

with open('news/analytics/most_common.json', 'w') as f:
    json.dump(most_common, f)

