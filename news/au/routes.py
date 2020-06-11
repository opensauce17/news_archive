from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from flask_user import login_required
from datetime import datetime, date, timedelta
from sqlalchemy import and_
from news.models import au_news


au = Blueprint('au', __name__)

@au.route('/au/search', methods=['GET', 'POST'])
def search():
    try:
        search_date = request.args.get('date')
        news_type = request.args.get('newstype')
        date = datetime.strptime(search_date, "%Y-%m-%d")
        full_date = date.strftime("%d %B, %Y")

        if news_type == 'headlines':
            headlines = au_news.query.filter(and_(au_news.news_type == 'headlines', au_news.publishedAt.like
            (f'%{search_date}%'))).order_by(au_news.publishedAt.desc())

            return render_template('au/search.html', headlines=headlines, today=full_date, news_type=news_type)

        elif news_type == 'business':
            business = au_news.query.filter(and_(au_news.news_type == 'business', au_news.publishedAt.like
            (f'%{search_date}%'))).order_by(au_news.publishedAt.desc())

            return render_template('au/search.html', business=business, today=full_date, news_type=news_type)

        elif news_type == 'technology':
            technology = au_news.query.filter(and_(au_news.news_type == 'technology', au_news.publishedAt.like
            (f'%{search_date}%'))).order_by(au_news.publishedAt.desc())

            return render_template('au/search.html', technology=technology, today=full_date, news_type=news_type)

        elif news_type == 'health':
            health = au_news.query.filter(and_(au_news.news_type == 'health', au_news.publishedAt.like
            (f'%{search_date}%'))).order_by(au_news.publishedAt.desc())

            return render_template('au/search.html', health=health, today=full_date, news_type=news_type)

        elif news_type == 'science':
            science = au_news.query.filter(and_(au_news.news_type == 'science', au_news.publishedAt.like
            (f'%{search_date}%'))).order_by(au_news.publishedAt.desc())

            return render_template('au/search.html', science=science, today=full_date, news_type=news_type)

        elif news_type == 'sports':
            sports = au_news.query.filter(and_(au_news.news_type == 'sports', au_news.publishedAt.like
            (f'%{search_date}%'))).order_by(au_news.publishedAt.desc())

            return render_template('au/search.html', sports=sports, today=full_date, news_type=news_type)

        elif news_type == 'entertainment':
            entertainment = au_news.query.filter(and_(au_news.news_type == 'entertainment', au_news.publishedAt.like
            (f'%{search_date}%'))).order_by(au_news.publishedAt.desc())

            return render_template('au/search.html', entertainment=entertainment, today=full_date, news_type=news_type)
    except ValueError:
        return render_template('au/error.html')



@au.route('/au/country', methods=['GET', 'POST'])
def index_country():

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = au_news.query.filter(and_(au_news.news_type == 'headlines', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('au/index.html', headlines=headlines, today=today, news_type=news_type)


@au.route('/au/', methods=['GET', 'POST'])
@login_required
def index():

    if request.method == 'POST':
        return redirect(url_for('/au/search'))

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = au_news.query.filter(and_(au_news.news_type == 'headlines', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('au/index.html', headlines=headlines, today=today, news_type=news_type)

@au.route('/au/business', methods=['GET', 'POST'])
@login_required
def business():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    business = au_news.query.filter(and_(au_news.news_type == 'business', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'business'

    return render_template('au/business.html', business=business, today=today, news_type=news_type)


@au.route('/au/technology', methods=['GET', 'POST'])
@login_required
def technology():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    technology = au_news.query.filter(and_(au_news.news_type == 'technology', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'technology'

    return render_template('au/technology.html', technology=technology, today=today, news_type=news_type)

@au.route('/au/health', methods=['GET', 'POST'])
@login_required
def health():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    health = au_news.query.filter(and_(au_news.news_type == 'health', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'health'

    return render_template('au/health.html', health=health, today=today, news_type=news_type)

@au.route('/au/science', methods=['GET', 'POST'])
@login_required
def science():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    science = au_news.query.filter(and_(au_news.news_type == 'science', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'science'

    return render_template('au/science.html', science=science, today=today, news_type=news_type)

@au.route('/au/sports', methods=['GET', 'POST'])
@login_required
def sports():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    sports = au_news.query.filter(and_(au_news.news_type == 'sports', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'sports'

    return render_template('au/sports.html', sports=sports, today=today, news_type=news_type)

@au.route('/au/entertainment', methods=['GET', 'POST'])
@login_required
def entertainment():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    entertainment = au_news.query.filter(and_(au_news.news_type == 'entertainment', au_news.publishedAt
                                              .like(f'%{today_date}%'))).order_by(au_news.publishedAt.desc())
    news_type = 'entertainment'

    return render_template('au/entertainment.html', entertainment=entertainment, today=today, news_type=news_type)
