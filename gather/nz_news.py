#! /usr/bin/env python

from newsapi import NewsApiClient
import sqlite3
from envious import load_env
import os

os.environ['ENV_FILE'] = os.path.dirname(os.path.abspath(__file__)) + '/.env'
load_env()
api_key = os.getenv('API_KEY')


newsapi = NewsApiClient(api_key=api_key)


### DATABASE INSERTS ###
def sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location):

    try:
        sqliteConnection = sqlite3.connect('/opt/news_archive/news/db/db.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO nz_news
                                                 ('source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', content, news_type, location)
                                                  VALUES
                                                 (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        count = cursor.execute(sqlite_insert_query,
                              (source, author, title, description, url, urlToImage, publishedAt, content, news_type, location))

        sqliteConnection.commit()
        print("Record inserted successfully into nz_news table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


### NEW ZEALAND ####

def nz_top_headlines():

    nz_top_headlines = newsapi.get_top_headlines(language='en',country='nz')

    for each_article in nz_top_headlines['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'headlines'
        location = 'New Zealand'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def nz_business():

    nz_business = newsapi.get_top_headlines(category='business', language='en', country='nz')


    for each_article in nz_business['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'business'
        location = 'New Zealand'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def nz_technology():

    nz_technology = newsapi.get_top_headlines(category='technology', language='en', country='nz')

    for each_article in nz_technology['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'technology'
        location = 'New Zealand'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)


def nz_health():

    nz_health = newsapi.get_top_headlines(category='health', language='en', country='nz')

    for each_article in nz_health['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'health'
        location = 'New Zealand'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)


def nz_science():

    nz_science = newsapi.get_top_headlines(category='science', language='en', country='nz')

    for each_article in nz_science['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'science'
        location = 'New Zealand'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def nz_sports():

    nz_sports = newsapi.get_top_headlines(category='sports', language='en', country='nz')

    for each_article in nz_sports['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'sports'
        location = 'New Zealand'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def nz_entertainment():

    nz_entertainment = newsapi.get_top_headlines(category='entertainment', language='en', country='nz')

    for each_article in nz_entertainment['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'entertainment'
        location = 'New Zealand'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

### END NEW ZEALAND ###

def main():

    nz_top_headlines()
    nz_business()
    nz_health()
    nz_science()
    nz_technology()
    nz_sports()
    nz_entertainment()


if __name__ == '__main__':
    main()



