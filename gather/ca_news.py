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

        sqlite_insert_query = """INSERT INTO ca_news
                                                 ('source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', content, news_type)
                                                  VALUES
                                                 (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        count = cursor.execute(sqlite_insert_query,
                              (source, author, title, description, url, urlToImage, publishedAt, content, news_type))

        sqliteConnection.commit()
        print("Record inserted successfully into ca_news table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


### SOUTH AFRICA ####

def ca_top_headlines():

    ca_top_headlines = newsapi.get_top_headlines(language='en',country='ca')

    for each_article in ca_top_headlines['articles']:
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

def ca_business():

    ca_business = newsapi.get_top_headlines(category='business', language='en', country='ca')


    for each_article in ca_business['articles']:
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

def ca_technology():

    ca_technology = newsapi.get_top_headlines(category='technology', language='en', country='ca')

    for each_article in ca_technology['articles']:
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


def ca_health():

    ca_health = newsapi.get_top_headlines(category='health', language='en', country='ca')

    for each_article in ca_health['articles']:
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


def ca_science():

    ca_science = newsapi.get_top_headlines(category='science', language='en', country='ca')

    for each_article in ca_science['articles']:
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

def ca_sports():

    ca_sports = newsapi.get_top_headlines(category='sports', language='en', country='ca')

    for each_article in ca_sports['articles']:
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

def ca_entertainment():

    ca_entertainment = newsapi.get_top_headlines(category='entertainment', language='en', country='ca')

    for each_article in ca_entertainment['articles']:
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

    ca_top_headlines()
    ca_business()
    ca_health()
    ca_science()
    ca_technology()
    ca_sports()
    ca_entertainment()


if __name__ == '__main__':
    main()



