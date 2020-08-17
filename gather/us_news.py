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

        sqlite_insert_query = """INSERT INTO us_news
                                                 ('source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', content, news_type, location)
                                                  VALUES
                                                 (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        count = cursor.execute(sqlite_insert_query,
                              (source, author, title, description, url, urlToImage, publishedAt, content, news_type, location))

        sqliteConnection.commit()
        print("Record inserted successfully into us_news table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


### UNITED STATES ####

def us_top_headlines():

    us_top_headlines = newsapi.get_top_headlines(language='en',country='us')

    for each_article in us_top_headlines['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'headlines'
        location = 'United States'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def us_business():

    us_business = newsapi.get_top_headlines(category='business', language='en', country='us')


    for each_article in us_business['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'business'
        location = 'United States'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def us_technology():

    us_technology = newsapi.get_top_headlines(category='technology', language='en', country='us')

    for each_article in us_technology['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'technology'
        location = 'United States'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)


def us_health():

    us_health = newsapi.get_top_headlines(category='health', language='en', country='us')

    for each_article in us_health['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'health'
        location = 'United States'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)


def us_science():

    us_science = newsapi.get_top_headlines(category='science', language='en', country='us')

    for each_article in us_science['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'science'
        location = 'United States'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def us_sports():

    us_sports = newsapi.get_top_headlines(category='sports', language='en', country='us')

    for each_article in us_sports['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'sports'
        location = 'United States'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

def us_entertainment():

    us_entertainment = newsapi.get_top_headlines(category='entertainment', language='en', country='us')

    for each_article in us_entertainment['articles']:
        source = each_article['source']['name']
        author = each_article['author']
        title = each_article['title']
        description = each_article['description']
        url = each_article['url']
        urlToImage = each_article['urlToImage']
        publishedAt = each_article['publishedAt']
        content = each_article['content']
        news_type = 'entertainment'
        location = 'United States'

        sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type, location)

### END UNITED STATES ###

def main():

    us_top_headlines()
    us_business()
    us_health()
    us_science()
    us_technology()
    us_sports()
    us_entertainment()


if __name__ == '__main__':
    main()



