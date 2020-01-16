from flask import Flask, render_template, request, url_for, redirect, message_flashed, flash, jsonify, session
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

class DataStore():
    headlines = 'headlines'

data = DataStore()

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


@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        search_date = request.args.get('date')
        news_type = request.args.get('newstype')
        date = datetime.strptime(search_date, "%Y-%m-%d")
        full_date = date.strftime("%d %B, %Y")

        if news_type == 'headlines':
            headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('search.html', headlines=headlines, today=full_date, news_type=news_type)

        elif news_type == 'business':
            business = za_news.query.filter(and_(za_news.news_type == 'business', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('search.html', business=business, today=full_date, news_type=news_type)

        elif news_type == 'technology':
            technology = za_news.query.filter(and_(za_news.news_type == 'technology', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('search.html', technology=technology, today=full_date, news_type=news_type)

        elif news_type == 'health':
            health = za_news.query.filter(and_(za_news.news_type == 'health', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('search.html', health=health, today=full_date, news_type=news_type)

        elif news_type == 'science':
            science = za_news.query.filter(and_(za_news.news_type == 'science', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('search.html', science=science, today=full_date, news_type=news_type)

        elif news_type == 'sports':
            sports = za_news.query.filter(and_(za_news.news_type == 'sports', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('search.html', sports=sports, today=full_date, news_type=news_type)

        elif news_type == 'entertainment':
            entertainment = za_news.query.filter(and_(za_news.news_type == 'entertainment', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('search.html', entertainment=entertainment, today=full_date, news_type=news_type)
    except ValueError:
        return render_template('error.html')



@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect(url_for('search'))

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('index.html', headlines=headlines, today=today)

@app.route('/business', methods=['GET', 'POST'])
def business():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    business = za_news.query.filter(and_(za_news.news_type == 'business', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('business.html', business=business, today=today)


@app.route('/technology', methods=['GET', 'POST'])
def technology():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    technology = za_news.query.filter(and_(za_news.news_type == 'technology', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('technology.html', technology=technology, today=today)

@app.route('/health', methods=['GET', 'POST'])
def health():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    health = za_news.query.filter(and_(za_news.news_type == 'health', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('health.html', health=health, today=today)

@app.route('/science', methods=['GET', 'POST'])
def science():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    science = za_news.query.filter(and_(za_news.news_type == 'science', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('science.html', science=science, today=today)

@app.route('/sports', methods=['GET', 'POST'])
def sports():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    sports = za_news.query.filter(and_(za_news.news_type == 'sports', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())

    return render_template('sports.html', sports=sports, today=today)

@app.route('/entertainment', methods=['GET', 'POST'])
def entertainment():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    entertainment = za_news.query.filter(and_(za_news.news_type == 'entertainment', za_news.publishedAt
                                              .like(f'%{today_date}%'))).order_by(za_news.publishedAt.desc())

    return render_template('entertainment.html', entertainment=entertainment, today=today)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5100, debug=True)
