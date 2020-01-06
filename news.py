#! /usr/bin/env python

from newsapi import NewsApiClient
import sqlite3

newsapi = NewsApiClient(api_key='ba7975edd96d4cecb9a952702565769a')



def sql_insert(source, author, title, description, url, urlToImage, publishedAt, content, news_type):

    try:
        sqliteConnection = sqlite3.connect('db.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO za_news
                                                 ('source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', content, news_type)
                                                  VALUES
                                                 (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        count = cursor.execute(sqlite_insert_query,
                              (source, author, title, description, url, urlToImage, publishedAt, content, news_type))

        sqliteConnection.commit()
        print("Record inserted successfully into za_news table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def za_top_headlines():

    za_top_headlines = newsapi.get_top_headlines(language='en',country='za')

    for each_article in za_top_headlines['articles']:
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

def za_business():

    za_business = newsapi.get_top_headlines(category='business', language='en', country='za')


    for each_article in za_business['articles']:
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

def za_technology():

    za_technology = newsapi.get_top_headlines(category='technology', language='en', country='za')

    for each_article in za_technology['articles']:
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

def za_sports():

    za_sports = newsapi.get_top_headlines(category='sports', language='en', country='za')

    for each_article in za_sports['articles']:
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

def za_entertainment():

    za_entertainment = newsapi.get_top_headlines(category='entertainment', language='en', country='za')

    for each_article in za_entertainment['articles']:
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

def main():

    za_top_headlines()
    za_business()
    za_technology()
    za_sports()
    za_entertainment()


if __name__ == '__main__':
    main()



