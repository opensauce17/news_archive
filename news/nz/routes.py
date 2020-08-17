from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from datetime import datetime, date, timedelta
from sqlalchemy import and_
from news.models import nz_news


nz = Blueprint('nz', __name__)

@nz.route('/nz/search', methods=['GET', 'POST'])
def search():
    try:
        search_date = request.args.get('date')
        news_type = request.args.get('newstype')
        date = datetime.strptime(search_date, "%Y-%m-%d")
        full_date = date.strftime("%d %B, %Y")

        if news_type == 'headlines':
            headlines = nz_news.query.filter(and_(nz_news.news_type == 'headlines', nz_news.publishedAt.like
            (f'%{search_date}%'))).order_by(nz_news.publishedAt.desc())

            return render_template('nz/search.html', headlines=headlines, today=full_date, news_type=news_type)

        elif news_type == 'business':
            business = nz_news.query.filter(and_(nz_news.news_type == 'business', nz_news.publishedAt.like
            (f'%{search_date}%'))).order_by(nz_news.publishedAt.desc())

            return render_template('nz/search.html', business=business, today=full_date, news_type=news_type)

        elif news_type == 'technology':
            technology = nz_news.query.filter(and_(nz_news.news_type == 'technology', nz_news.publishedAt.like
            (f'%{search_date}%'))).order_by(nz_news.publishedAt.desc())

            return render_template('nz/search.html', technology=technology, today=full_date, news_type=news_type)

        elif news_type == 'health':
            health = nz_news.query.filter(and_(nz_news.news_type == 'health', nz_news.publishedAt.like
            (f'%{search_date}%'))).order_by(nz_news.publishedAt.desc())

            return render_template('nz/search.html', health=health, today=full_date, news_type=news_type)

        elif news_type == 'science':
            science = nz_news.query.filter(and_(nz_news.news_type == 'science', nz_news.publishedAt.like
            (f'%{search_date}%'))).order_by(nz_news.publishedAt.desc())

            return render_template('nz/search.html', science=science, today=full_date, news_type=news_type)

        elif news_type == 'sports':
            sports = nz_news.query.filter(and_(nz_news.news_type == 'sports', nz_news.publishedAt.like
            (f'%{search_date}%'))).order_by(nz_news.publishedAt.desc())

            return render_template('nz/search.html', sports=sports, today=full_date, news_type=news_type)

        elif news_type == 'entertainment':
            entertainment = nz_news.query.filter(and_(nz_news.news_type == 'entertainment', nz_news.publishedAt.like
            (f'%{search_date}%'))).order_by(nz_news.publishedAt.desc())

            return render_template('nz/search.html', entertainment=entertainment, today=full_date, news_type=news_type)
    except ValueError:
        return render_template('nz/error.html', news_type=news_type)



@nz.route('/nz/country', methods=['GET', 'POST'])
def index_country():

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = nz_news.query.filter(and_(nz_news.news_type == 'headlines', nz_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(nz_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('nz/index.html', headlines=headlines, today=today, news_type=news_type)


@nz.route('/nz/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect(url_for('/nz/search'))

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = nz_news.query.filter(and_(nz_news.news_type == 'headlines', nz_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(nz_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('nz/index.html', headlines=headlines, today=today, news_type=news_type)

@nz.route('/nz/business', methods=['GET', 'POST'])
def business():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    business = nz_news.query.filter(and_(nz_news.news_type == 'business', nz_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(nz_news.publishedAt.desc())
    news_type = 'business'

    return render_template('nz/business.html', business=business, today=today, news_type=news_type)


@nz.route('/nz/technology', methods=['GET', 'POST'])
def technology():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    technology = nz_news.query.filter(and_(nz_news.news_type == 'technology', nz_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(nz_news.publishedAt.desc())
    news_type = 'technology'

    return render_template('nz/technology.html', technology=technology, today=today, news_type=news_type)

@nz.route('/nz/health', methods=['GET', 'POST'])
def health():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    health = nz_news.query.filter(and_(nz_news.news_type == 'health', nz_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(nz_news.publishedAt.desc())
    news_type = 'health'

    return render_template('nz/health.html', health=health, today=today, news_type=news_type)

@nz.route('/nz/science', methods=['GET', 'POST'])
def science():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    science = nz_news.query.filter(and_(nz_news.news_type == 'science', nz_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(nz_news.publishedAt.desc())
    news_type = 'science'

    return render_template('nz/science.html', science=science, today=today, news_type=news_type)

@nz.route('/nz/sports', methods=['GET', 'POST'])
def sports():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    sports = nz_news.query.filter(and_(nz_news.news_type == 'sports', nz_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(nz_news.publishedAt.desc())
    news_type = 'sports'

    return render_template('nz/sports.html', sports=sports, today=today, news_type=news_type)

@nz.route('/nz/entertainment', methods=['GET', 'POST'])
def entertainment():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    entertainment = nz_news.query.filter(and_(nz_news.news_type == 'entertainment', nz_news.publishedAt
                                              .like(f'%{today_date}%'))).order_by(nz_news.publishedAt.desc())
    news_type = 'entertainment'

    return render_template('nz/entertainment.html', entertainment=entertainment, today=today, news_type=news_type)
