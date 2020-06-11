from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from flask_user import login_required
from datetime import datetime
from sqlalchemy import and_
from news.models import za_news
from news.models import us_news
from news.models import au_news
from news.models import ca_news
from news.models import nz_news
from news.models import gb_news

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():

    return render_template('main/index.html')


@main.route('/country', methods=['GET', 'POST'])
def country():

    country = request.args.get('country')

    if country == "za":

        today = datetime.now().strftime("%d %B, %Y")
        today_date = datetime.now()
        today_date = str(today_date).split(" ", 1)[0]
        headlines = za_news.query.filter(
            and_(za_news.news_type == 'headlines', za_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(za_news.publishedAt.desc())
        news_type = 'headlines'

        return render_template('za/index.html', headlines=headlines, today=today, news_type=news_type)

    if country == "us":

        today = datetime.now().strftime("%d %B, %Y")
        today_date = datetime.now()
        today_date = str(today_date).split(" ", 1)[0]
        headlines = us_news.query.filter(
            and_(us_news.news_type == 'headlines', us_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(us_news.publishedAt.desc())
        news_type = 'headlines'


        return render_template('us/index.html', headlines=headlines, today=today, news_type=news_type)

    if country == "au":

        today = datetime.now().strftime("%d %B, %Y")
        today_date = datetime.now()
        today_date = str(today_date).split(" ", 1)[0]
        headlines = au_news.query.filter(
            and_(au_news.news_type == 'headlines', au_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(au_news.publishedAt.desc())
        news_type = 'headlines'


        return render_template('au/index.html', headlines=headlines, today=today, news_type=news_type)

    if country == "ca":

        today = datetime.now().strftime("%d %B, %Y")
        today_date = datetime.now()
        today_date = str(today_date).split(" ", 1)[0]
        headlines = ca_news.query.filter(
            and_(ca_news.news_type == 'headlines', ca_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(ca_news.publishedAt.desc())
        news_type = 'headlines'


        return render_template('ca/index.html', headlines=headlines, today=today, news_type=news_type)

    if country == "nz":

        today = datetime.now().strftime("%d %B, %Y")
        today_date = datetime.now()
        today_date = str(today_date).split(" ", 1)[0]
        headlines = nz_news.query.filter(
            and_(nz_news.news_type == 'headlines', nz_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(nz_news.publishedAt.desc())
        news_type = 'headlines'


        return render_template('nz/index.html', headlines=headlines, today=today, news_type=news_type)

    if country == "gb":

        today = datetime.now().strftime("%d %B, %Y")
        today_date = datetime.now()
        today_date = str(today_date).split(" ", 1)[0]
        headlines = gb_news.query.filter(
            and_(gb_news.news_type == 'headlines', gb_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(gb_news.publishedAt.desc())
        news_type = 'headlines'


        return render_template('gb/index.html', headlines=headlines, today=today, news_type=news_type)

@main.route('/au/', methods=['GET', 'POST'])
@login_required
def au_headlines():
    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    headlines = au_news.query.filter(and_(au_news.news_type == 'headlines', au_news.publishedAt.like(f'%{today_date}%')))\
        .order_by(au_news.publishedAt.desc())
    news_type = 'headlines'

    return render_template('au/index.html', headlines=headlines, today=today, news_type=news_type)