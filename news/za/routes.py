from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from datetime import datetime, date, timedelta
from sqlalchemy import and_
from news.models import za_news


za = Blueprint('za', __name__)

@za.route('/za/search', methods=['GET', 'POST'])
def search():
    try:
        search_date = request.args.get('date')
        news_type = request.args.get('newstype')
        date = datetime.strptime(search_date, "%Y-%m-%d")
        full_date = date.strftime("%d %B, %Y")

        if news_type == 'headlines':
            headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('za/search.html', headlines=headlines, today=full_date, news_type=news_type)

        elif news_type == 'business':
            business = za_news.query.filter(and_(za_news.news_type == 'business', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('za/search.html', business=business, today=full_date, news_type=news_type)

        elif news_type == 'technology':
            technology = za_news.query.filter(and_(za_news.news_type == 'technology', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('za/search.html', technology=technology, today=full_date, news_type=news_type)

        elif news_type == 'health':
            health = za_news.query.filter(and_(za_news.news_type == 'health', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('za/search.html', health=health, today=full_date, news_type=news_type)

        elif news_type == 'science':
            science = za_news.query.filter(and_(za_news.news_type == 'science', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('za/search.html', science=science, today=full_date, news_type=news_type)

        elif news_type == 'sports':
            sports = za_news.query.filter(and_(za_news.news_type == 'sports', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('za/search.html', sports=sports, today=full_date, news_type=news_type)

        elif news_type == 'entertainment':
            entertainment = za_news.query.filter(and_(za_news.news_type == 'entertainment', za_news.publishedAt.like
            (f'%{search_date}%'))).order_by(za_news.publishedAt.desc())

            return render_template('za/search.html', entertainment=entertainment, today=full_date, news_type=news_type)
    except ValueError:
        return render_template('za/error.html')



@za.route('/za/country', methods=['GET', 'POST'])
def index_country():

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('za/index.html', headlines=headlines, today=today, news_type=news_type)


@za.route('/za/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect(url_for('/za/search'))

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('za/index.html', headlines=headlines, today=today, news_type=news_type)

@za.route('/za/business', methods=['GET', 'POST'])
def business():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    business = za_news.query.filter(and_(za_news.news_type == 'business', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())
    news_type = 'business'

    return render_template('za/business.html', business=business, today=today, news_type=news_type)


@za.route('/za/technology', methods=['GET', 'POST'])
def technology():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    technology = za_news.query.filter(and_(za_news.news_type == 'technology', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())
    news_type = 'technology'

    return render_template('za/technology.html', technology=technology, today=today, news_type=news_type)

@za.route('/za/health', methods=['GET', 'POST'])
def health():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    health = za_news.query.filter(and_(za_news.news_type == 'health', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())
    news_type = 'health'

    return render_template('za/health.html', health=health, today=today, news_type=news_type)

@za.route('/za/science', methods=['GET', 'POST'])
def science():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    science = za_news.query.filter(and_(za_news.news_type == 'science', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())
    news_type = 'science'

    return render_template('za/science.html', science=science, today=today, news_type=news_type)

@za.route('/za/sports', methods=['GET', 'POST'])
def sports():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    sports = za_news.query.filter(and_(za_news.news_type == 'sports', za_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(za_news.publishedAt.desc())
    news_type = 'sports'

    return render_template('za/sports.html', sports=sports, today=today, news_type=news_type)

@za.route('/za/entertainment', methods=['GET', 'POST'])
def entertainment():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    entertainment = za_news.query.filter(and_(za_news.news_type == 'entertainment', za_news.publishedAt
                                              .like(f'%{today_date}%'))).order_by(za_news.publishedAt.desc())
    news_type = 'entertainment'

    return render_template('za/entertainment.html', entertainment=entertainment, today=today, news_type=news_type)
