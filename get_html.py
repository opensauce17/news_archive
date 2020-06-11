#! /usr/bin/env python

from bs4 import BeautifulSoup as soup
#from urllib.request import urlopen as uReq
import requests
import sqlite3
import json
from requests.exceptions import ConnectionError, TooManyRedirects, ReadTimeout

from news.models import au_news
from sqlalchemy import select


### DATABASE INSERTS ###
def sql_insert(wb_url, page_url):

    try:
        conn = sqlite3.connect('news/db/db.db')
        cur = conn.cursor()
        print("Successfully Connected to SQLite")

        cur.execute('''UPDATE au_news SET archive_link = ? WHERE url = ?''', (wb_url, page_url))

        #conn.commit()
        print("Record inserted successfully into au_news table ", cur.rowcount)
        #conn.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    #finally:
    #    if (conn):
    #        conn.close()
    #        print("The SQLite connection is closed")


def get_url_html():

    conn = sqlite3.connect('news/db/db.db')
    cur = conn.cursor()

    urls = []

    for row in cur.execute('SELECT url FROM au_news'):
        urls.append(row[0])

    print(len(urls))
    #     page_url = row[0]
    #     wayback_get_url = "https://archive.org/wayback/available?url={}".format(page_url)
    #     get_wayback = requests.get(wayback_get_url).json()
    #     try:
    #         wb_url = get_wayback['archived_snapshots']['closest']['url']
    #         print('Adding ' + wb_url + 'to the database for ' + page_url)
    #         sql_insert(wb_url, page_url)
    #     except KeyError:
    #         wayback_url = 'https://pragma.archivelab.org'
    #         news_url = get_wayback['url']
    #         data = {"url": "" + news_url + "", "annotation": {"id": "lst-ib", "message": "world news archive"}}
    #
    #         x = requests.post(wayback_url, data=data)
    #         x_json = json.loads(x.text)
    #
    #         try: 
    #             archive_url = x_json['wayback_id']
    #             print('This is an added URL: ' + get_wayback['url'])
    #             #print(get_wayback['url'])
    #         except KeyError:
    #             pass
    #
    # conn.commit()


        #page_html = page.text
        #cur2.execute('''UPDATE au_news SET html = ? WHERE url = ?''', (page_html, page_url))
        #conn.commit()




def main():

    get_url_html()

if __name__ == '__main__':
    main()





