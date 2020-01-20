from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from datetime import datetime
from sqlalchemy import and_
from news.models import za_news

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
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
        return render_template('za/index.html')


