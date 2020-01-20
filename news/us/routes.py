from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from datetime import datetime, date, timedelta
from sqlalchemy import and_
from news.models import us_news


us = Blueprint('us', __name__)

@us.route('/us/search', methods=['GET', 'POST'])
def search():
    try:
        search_date = request.args.get('date')
        news_type = request.args.get('newstype')
        date = datetime.strptime(search_date, "%Y-%m-%d")
        full_date = date.strftime("%d %B, %Y")

        if news_type == 'headlines':
            headlines = us_news.query.filter(and_(us_news.news_type == 'headlines', us_news.publishedAt.like
            (f'%{search_date}%'))).order_by(us_news.publishedAt.desc())

            return render_template('us/search.html', headlines=headlines, today=full_date, news_type=news_type)

        elif news_type == 'business':
            business = us_news.query.filter(and_(us_news.news_type == 'business', us_news.publishedAt.like
            (f'%{search_date}%'))).order_by(us_news.publishedAt.desc())

            return render_template('us/search.html', business=business, today=full_date, news_type=news_type)

        elif news_type == 'technology':
            technology = us_news.query.filter(and_(us_news.news_type == 'technology', us_news.publishedAt.like
            (f'%{search_date}%'))).order_by(us_news.publishedAt.desc())

            return render_template('us/search.html', technology=technology, today=full_date, news_type=news_type)

        elif news_type == 'health':
            health = us_news.query.filter(and_(us_news.news_type == 'health', us_news.publishedAt.like
            (f'%{search_date}%'))).order_by(us_news.publishedAt.desc())

            return render_template('us/search.html', health=health, today=full_date, news_type=news_type)

        elif news_type == 'science':
            science = us_news.query.filter(and_(us_news.news_type == 'science', us_news.publishedAt.like
            (f'%{search_date}%'))).order_by(us_news.publishedAt.desc())

            return render_template('us/search.html', science=science, today=full_date, news_type=news_type)

        elif news_type == 'sports':
            sports = us_news.query.filter(and_(us_news.news_type == 'sports', us_news.publishedAt.like
            (f'%{search_date}%'))).order_by(us_news.publishedAt.desc())

            return render_template('us/search.html', sports=sports, today=full_date, news_type=news_type)

        elif news_type == 'entertainment':
            entertainment = us_news.query.filter(and_(us_news.news_type == 'entertainment', us_news.publishedAt.like
            (f'%{search_date}%'))).order_by(us_news.publishedAt.desc())

            return render_template('us/search.html', entertainment=entertainment, today=full_date, news_type=news_type)
    except ValueError:
        return render_template('us/error.html')



@us.route('/us/country', methods=['GET', 'POST'])
def index_country():

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = us_news.query.filter(and_(us_news.news_type == 'headlines', us_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(us_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('us/index.html', headlines=headlines, today=today, news_type=news_type)


@us.route('/us/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect(url_for('/us/search'))

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = us_news.query.filter(and_(us_news.news_type == 'headlines', us_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(us_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('us/index.html', headlines=headlines, today=today, news_type=news_type)

@us.route('/us/business', methods=['GET', 'POST'])
def business():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    business = us_news.query.filter(and_(us_news.news_type == 'business', us_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(us_news.publishedAt.desc())
    news_type = 'business'

    return render_template('us/business.html', business=business, today=today, news_type=news_type)


@us.route('/us/technology', methods=['GET', 'POST'])
def technology():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    technology = us_news.query.filter(and_(us_news.news_type == 'technology', us_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(us_news.publishedAt.desc())
    news_type = 'technology'

    return render_template('us/technology.html', technology=technology, today=today, news_type=news_type)

@us.route('/us/health', methods=['GET', 'POST'])
def health():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    health = us_news.query.filter(and_(us_news.news_type == 'health', us_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(us_news.publishedAt.desc())
    news_type = 'health'

    return render_template('us/health.html', health=health, today=today, news_type=news_type)

@us.route('/us/science', methods=['GET', 'POST'])
def science():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    science = us_news.query.filter(and_(us_news.news_type == 'science', us_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(us_news.publishedAt.desc())
    news_type = 'science'

    return render_template('us/science.html', science=science, today=today, news_type=news_type)

@us.route('/us/sports', methods=['GET', 'POST'])
def sports():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    sports = us_news.query.filter(and_(us_news.news_type == 'sports', us_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(us_news.publishedAt.desc())
    news_type = 'sports'

    return render_template('us/sports.html', sports=sports, today=today, news_type=news_type)

@us.route('/us/entertainment', methods=['GET', 'POST'])
def entertainment():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    entertainment = us_news.query.filter(and_(us_news.news_type == 'entertainment', us_news.publishedAt
                                              .like(f'%{today_date}%'))).order_by(us_news.publishedAt.desc())
    news_type = 'entertainment'

    return render_template('us/entertainment.html', entertainment=entertainment, today=today, news_type=news_type)
