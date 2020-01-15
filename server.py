from flask import Flask, render_template, request, url_for, redirect, message_flashed, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, timedelta
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

@app.route('/za/')
def index():

    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    yesterday = date.today() - timedelta(days=1)
    headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like(f'%{today}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('index.html', headlines=headlines)

@app.route('/za/business')
def business():
    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    yesterday = date.today() - timedelta(days=1)
    business = za_news.query.filter(and_(za_news.news_type == 'business', za_news.publishedAt.like(f'%{today}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('business.html', business=business)


@app.route('/za/technology')
def technology():
    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    yesterday = date.today() - timedelta(days=1)
    technology = za_news.query.filter(and_(za_news.news_type == 'technology', za_news.publishedAt.like(f'%{today}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('technology.html', technology=technology)

@app.route('/za/sports')
def sports():
    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    yesterday = date.today() - timedelta(days=1)
    sports = za_news.query.filter(and_(za_news.news_type == 'sports', za_news.publishedAt.like(f'%{today}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('sports.html', sports=sports)


@app.route('/za/health')
def health():
    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    yesterday = date.today() - timedelta(days=1)
    health = za_news.query.filter(and_(za_news.news_type == 'health', za_news.publishedAt.like(f'%{today}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('health.html', health=health)

@app.route('/za/science')
def science():
    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    yesterday = date.today() - timedelta(days=1)
    science = za_news.query.filter(and_(za_news.news_type == 'science', za_news.publishedAt.like(f'%{today}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('science.html', science=science)


@app.route('/za/entertainment')
def entertainment():
    today = datetime.now()
    today = str(today).split(" ", 1)[0]
    yesterday = date.today() - timedelta(days=1)
    entertainment = za_news.query.filter(and_(za_news.news_type == 'entertainment', za_news.publishedAt
                                              .like(f'%{today}%'))).order_by(za_news.publishedAt.desc())

    return render_template('entertainment.html', entertainment=entertainment)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5100, debug=True)
