from flask import Flask, render_template, request, url_for, redirect, message_flashed, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from sqlalchemy import and_

import sqlite3

app = Flask(__name__)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CGVC39xyCk8lUmR6DzT_LA'

db = SQLAlchemy(app)

db.init_app(app)


# Define the za_news data-model
class za_news(db.Model):
    __tablename__ = 'za_news'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
    urlToImage = db.Column(db.String(100))
    #publishedAt = db.Column(db.DateTime)
    publishedAt = db.Column(db.Text)
    #publishedAt = db.Column(db.String(100))
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))

@app.route('/')
def index():

    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    print(today)

    #headlines = za_news.query.filter_by(news_type='headlines').all()
    headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like('%'today'%')).all()
    #print(posts)
    for headline in headlines:
        #print(headline.publishedAt)
        source = headline.source
        author = headline.author
        title = headline.title
        description = headline.description
        url = headline.url
        image = headline.urlToImage
        date = headline.publishedAt
        content = headline.content

        # print(source)
        # print(author)
        # print(title)
        # print(description)
        # print(url)
        # print(image)
        # print(date)
        # print(content)



    return render_template('index.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5100, debug=True)
