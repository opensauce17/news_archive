from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from datetime import datetime, date, timedelta
from sqlalchemy import and_
from news.models import gb_news


gb = Blueprint('gb', __name__)

@gb.route('/gb/search', methods=['GET', 'POST'])
def search():
    try:
        search_date = request.args.get('date')
        news_type = request.args.get('newstype')
        date = datetime.strptime(search_date, "%Y-%m-%d")
        full_date = date.strftime("%d %B, %Y")

        if news_type == 'headlines':
            headlines = gb_news.query.filter(and_(gb_news.news_type == 'headlines', gb_news.publishedAt.like
            (f'%{search_date}%'))).order_by(gb_news.publishedAt.desc())

            return render_template('gb/search.html', headlines=headlines, today=full_date, news_type=news_type)

        elif news_type == 'business':
            business = gb_news.query.filter(and_(gb_news.news_type == 'business', gb_news.publishedAt.like
            (f'%{search_date}%'))).order_by(gb_news.publishedAt.desc())

            return render_template('gb/search.html', business=business, today=full_date, news_type=news_type)

        elif news_type == 'technology':
            technology = gb_news.query.filter(and_(gb_news.news_type == 'technology', gb_news.publishedAt.like
            (f'%{search_date}%'))).order_by(gb_news.publishedAt.desc())

            return render_template('gb/search.html', technology=technology, today=full_date, news_type=news_type)

        elif news_type == 'health':
            health = gb_news.query.filter(and_(gb_news.news_type == 'health', gb_news.publishedAt.like
            (f'%{search_date}%'))).order_by(gb_news.publishedAt.desc())

            return render_template('gb/search.html', health=health, today=full_date, news_type=news_type)

        elif news_type == 'science':
            science = gb_news.query.filter(and_(gb_news.news_type == 'science', gb_news.publishedAt.like
            (f'%{search_date}%'))).order_by(gb_news.publishedAt.desc())

            return render_template('gb/search.html', science=science, today=full_date, news_type=news_type)

        elif news_type == 'sports':
            sports = gb_news.query.filter(and_(gb_news.news_type == 'sports', gb_news.publishedAt.like
            (f'%{search_date}%'))).order_by(gb_news.publishedAt.desc())

            return render_template('gb/search.html', sports=sports, today=full_date, news_type=news_type)

        elif news_type == 'entertainment':
            entertainment = gb_news.query.filter(and_(gb_news.news_type == 'entertainment', gb_news.publishedAt.like
            (f'%{search_date}%'))).order_by(gb_news.publishedAt.desc())

            return render_template('gb/search.html', entertainment=entertainment, today=full_date, news_type=news_type)
    except ValueError:
        return render_template('gb/error.html', news_type=news_type)



@gb.route('/gb/country', methods=['GET', 'POST'])
def index_country():

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = gb_news.query.filter(and_(gb_news.news_type == 'headlines', gb_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(gb_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('gb/index.html', headlines=headlines, today=today, news_type=news_type)


@gb.route('/gb/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect(url_for('/gb/search'))

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = gb_news.query.filter(and_(gb_news.news_type == 'headlines', gb_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(gb_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('gb/index.html', headlines=headlines, today=today, news_type=news_type)

@gb.route('/gb/business', methods=['GET', 'POST'])
def business():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    business = gb_news.query.filter(and_(gb_news.news_type == 'business', gb_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(gb_news.publishedAt.desc())
    news_type = 'business'

    return render_template('gb/business.html', business=business, today=today, news_type=news_type)


@gb.route('/gb/technology', methods=['GET', 'POST'])
def technology():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    technology = gb_news.query.filter(and_(gb_news.news_type == 'technology', gb_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(gb_news.publishedAt.desc())
    news_type = 'technology'

    return render_template('gb/technology.html', technology=technology, today=today, news_type=news_type)

@gb.route('/gb/health', methods=['GET', 'POST'])
def health():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    health = gb_news.query.filter(and_(gb_news.news_type == 'health', gb_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(gb_news.publishedAt.desc())
    news_type = 'health'

    return render_template('gb/health.html', health=health, today=today, news_type=news_type)

@gb.route('/gb/science', methods=['GET', 'POST'])
def science():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    science = gb_news.query.filter(and_(gb_news.news_type == 'science', gb_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(gb_news.publishedAt.desc())
    news_type = 'science'

    return render_template('gb/science.html', science=science, today=today, news_type=news_type)

@gb.route('/gb/sports', methods=['GET', 'POST'])
def sports():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    sports = gb_news.query.filter(and_(gb_news.news_type == 'sports', gb_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(gb_news.publishedAt.desc())
    news_type = 'sports'

    return render_template('gb/sports.html', sports=sports, today=today, news_type=news_type)

@gb.route('/gb/entertainment', methods=['GET', 'POST'])
def entertainment():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    entertainment = gb_news.query.filter(and_(gb_news.news_type == 'entertainment', gb_news.publishedAt
                                              .like(f'%{today_date}%'))).order_by(gb_news.publishedAt.desc())
    news_type = 'entertainment'

    return render_template('gb/entertainment.html', entertainment=entertainment, today=today, news_type=news_type)
