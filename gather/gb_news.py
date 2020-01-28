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
def sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type):

    try:
        sqliteConnection = sqlite3.connect('/opt/news_archive/news/db/db.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO gb_news
                                                 ('source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', content, news_type)
                                                  VALUES
                                                 (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        count = cursor.execute(sqlite_insert_query,
                              (source, author, title, description, url, urlToImage, publishedAt, content, news_type))

        sqliteConnection.commit()
        print("Record inserted successfully into gb_news table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


### SOUTH AFRICA ####

def gb_top_headlines():

    gb_top_headlines = newsapi.get_top_headlines(language='en',country='gb')

    for each_article in gb_top_headlines['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'headlines'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type)

def gb_business():

    gb_business = newsapi.get_top_headlines(category='business', language='en', country='gb')


    for each_article in gb_business['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'business'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type)

def gb_technology():

    gb_technology = newsapi.get_top_headlines(category='technology', language='en', country='gb')

    for each_article in gb_technology['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'technology'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type)


def gb_health():

    gb_health = newsapi.get_top_headlines(category='health', language='en', country='gb')

    for each_article in gb_health['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'health'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type)


def gb_science():

    gb_science = newsapi.get_top_headlines(category='science', language='en', country='gb')

    for each_article in gb_science['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'science'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type)

def gb_sports():

    gb_sports = newsapi.get_top_headlines(category='sports', language='en', country='gb')

    for each_article in gb_sports['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'sports'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type)

def gb_entertainment():

    gb_entertainment = newsapi.get_top_headlines(category='entertainment', language='en', country='gb')

    for each_article in gb_entertainment['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'entertainment'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type)

### END SOUTH AFRICA ###

def main():

    gb_top_headlines()
    gb_business()
    gb_health()
    gb_science()
    gb_technology()
    gb_sports()
    gb_entertainment()


if __name__ == '__main__':
    main()



