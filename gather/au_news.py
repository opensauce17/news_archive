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

        sqlite_insert_query = """INSERT INTO au_news
                                                 ('source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', content, news_type, location)
                                                  VALUES
                                                 (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        count = cursor.execute(sqlite_insert_query,
                              (source, author, title, description, url, urlToImage, publishedAt, content, news_type, location))

        sqliteConnection.commit()
        print("Record inserted successfully into au_news table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


### AUSTRALIA ####

def au_top_headlines():

    au_top_headlines = newsapi.get_top_headlines(language='en',country='au')

    for each_article in au_top_headlines['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'headlines'
        location = 'Australia'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def au_business():

    au_business = newsapi.get_top_headlines(category='business', language='en', country='au')


    for each_article in au_business['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'business'
        location = 'Australia'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def au_technology():

    au_technology = newsapi.get_top_headlines(category='technology', language='en', country='au')

    for each_article in au_technology['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'technology'
        location = 'Australia'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)


def au_health():

    au_health = newsapi.get_top_headlines(category='health', language='en', country='au')

    for each_article in au_health['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'health'
        location = 'Australia'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)


def au_science():

    au_science = newsapi.get_top_headlines(category='science', language='en', country='au')

    for each_article in au_science['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'science'
        location = 'Australia'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def au_sports():

    au_sports = newsapi.get_top_headlines(category='sports', language='en', country='au')

    for each_article in au_sports['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'sports'
        location = 'Australia'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def au_entertainment():

    au_entertainment = newsapi.get_top_headlines(category='entertainment', language='en', country='au')

    for each_article in au_entertainment['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'entertainment'
        location = 'Australia'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

### END AUSTRALIA ###

def main():

    au_top_headlines()
    au_business()
    au_health()
    au_science()
    au_technology()
    au_sports()
    au_entertainment()


if __name__ == '__main__':
    main()



