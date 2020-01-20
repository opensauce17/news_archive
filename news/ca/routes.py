from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from datetime import datetime, date, timedelta
from sqlalchemy import and_
from news.models import ca_news


ca = Blueprint('ca', __name__)

@ca.route('/ca/search', methods=['GET', 'POST'])
def search():
    try:
        search_date = request.args.get('date')
        news_type = request.args.get('newstype')
        date = datetime.strptime(search_date, "%Y-%m-%d")
        full_date = date.strftime("%d %B, %Y")

        if news_type == 'headlines':
            headlines = ca_news.query.filter(and_(ca_news.news_type == 'headlines', ca_news.publishedAt.like
            (f'%{search_date}%'))).order_by(ca_news.publishedAt.desc())

            return render_template('ca/search.html', headlines=headlines, today=full_date, news_type=news_type)

        elif news_type == 'business':
            business = ca_news.query.filter(and_(ca_news.news_type == 'business', ca_news.publishedAt.like
            (f'%{search_date}%'))).order_by(ca_news.publishedAt.desc())

            return render_template('ca/search.html', business=business, today=full_date, news_type=news_type)

        elif news_type == 'technology':
            technology = ca_news.query.filter(and_(ca_news.news_type == 'technology', ca_news.publishedAt.like
            (f'%{search_date}%'))).order_by(ca_news.publishedAt.desc())

            return render_template('ca/search.html', technology=technology, today=full_date, news_type=news_type)

        elif news_type == 'health':
            health = ca_news.query.filter(and_(ca_news.news_type == 'health', ca_news.publishedAt.like
            (f'%{search_date}%'))).order_by(ca_news.publishedAt.desc())

            return render_template('ca/search.html', health=health, today=full_date, news_type=news_type)

        elif news_type == 'science':
            science = ca_news.query.filter(and_(ca_news.news_type == 'science', ca_news.publishedAt.like
            (f'%{search_date}%'))).order_by(ca_news.publishedAt.desc())

            return render_template('ca/search.html', science=science, today=full_date, news_type=news_type)

        elif news_type == 'sports':
            sports = ca_news.query.filter(and_(ca_news.news_type == 'sports', ca_news.publishedAt.like
            (f'%{search_date}%'))).order_by(ca_news.publishedAt.desc())

            return render_template('ca/search.html', sports=sports, today=full_date, news_type=news_type)

        elif news_type == 'entertainment':
            entertainment = ca_news.query.filter(and_(ca_news.news_type == 'entertainment', ca_news.publishedAt.like
            (f'%{search_date}%'))).order_by(ca_news.publishedAt.desc())

            return render_template('ca/search.html', entertainment=entertainment, today=full_date, news_type=news_type)
    except ValueError:
        return render_template('ca/error.html')



@ca.route('/ca/country', methods=['GET', 'POST'])
def index_country():

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = ca_news.query.filter(and_(ca_news.news_type == 'headlines', ca_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(ca_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('ca/index.html', headlines=headlines, today=today, news_type=news_type)


@ca.route('/ca/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect(url_for('/ca/search'))

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = ca_news.query.filter(and_(ca_news.news_type == 'headlines', ca_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(ca_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('ca/index.html', headlines=headlines, today=today, news_type=news_type)

@ca.route('/ca/business', methods=['GET', 'POST'])
def business():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    business = ca_news.query.filter(and_(ca_news.news_type == 'business', ca_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(ca_news.publishedAt.desc())
    news_type = 'business'

    return render_template('ca/business.html', business=business, today=today, news_type=news_type)


@ca.route('/ca/technology', methods=['GET', 'POST'])
def technology():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    technology = ca_news.query.filter(and_(ca_news.news_type == 'technology', ca_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(ca_news.publishedAt.desc())
    news_type = 'technology'

    return render_template('ca/technology.html', technology=technology, today=today, news_type=news_type)

@ca.route('/ca/health', methods=['GET', 'POST'])
def health():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    health = ca_news.query.filter(and_(ca_news.news_type == 'health', ca_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(ca_news.publishedAt.desc())
    news_type = 'health'

    return render_template('ca/health.html', health=health, today=today, news_type=news_type)

@ca.route('/ca/science', methods=['GET', 'POST'])
def science():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    science = ca_news.query.filter(and_(ca_news.news_type == 'science', ca_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(ca_news.publishedAt.desc())
    news_type = 'science'

    return render_template('ca/science.html', science=science, today=today, news_type=news_type)

@ca.route('/ca/sports', methods=['GET', 'POST'])
def sports():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    sports = ca_news.query.filter(and_(ca_news.news_type == 'sports', ca_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(ca_news.publishedAt.desc())
    news_type = 'sports'

    return render_template('ca/sports.html', sports=sports, today=today, news_type=news_type)

@ca.route('/ca/entertainment', methods=['GET', 'POST'])
def entertainment():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    entertainment = ca_news.query.filter(and_(ca_news.news_type == 'entertainment', ca_news.publishedAt
                                              .like(f'%{today_date}%'))).order_by(ca_news.publishedAt.desc())
    news_type = 'entertainment'

    return render_template('ca/entertainment.html', entertainment=entertainment, today=today, news_type=news_type)
