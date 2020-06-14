from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from flask_user import login_required
from flask_login import current_user
from datetime import datetime
from sqlalchemy import and_, tuple_
from news.models import za_news
from news.models import us_news
from news.models import au_news
from news.models import ca_news
from news.models import nz_news
from news.models import gb_news
from news.models import User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():

    username = current_user.username

    user_data = User.query.filter(
        and_(User.username == username)
    )

    user_defaults = []

    for i in user_data:
        user_defaults.append(i.pref_location)
        user_defaults.append(i.pref_news_type)

    location = user_defaults[0]

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    news_type = user_defaults[1]
    default_settings = []
    if location == "us":
        defaults = us_news.query.filter(
            and_(us_news.news_type == news_type, us_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(us_news.publishedAt.desc())
        default_settings.append(defaults)
    if location == 'za':
        defaults = za_news.query.filter(
            and_(za_news.news_type == news_type, za_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(za_news.publishedAt.desc())
        default_settings.append(defaults)
    if location == 'au':
        defaults = au_news.query.filter(
            and_(au_news.news_type == news_type, au_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(au_news.publishedAt.desc())
        default_settings.append(defaults)
    if location == 'ca':
        defaults = ca_news.query.filter(
            and_(ca_news.news_type == news_type, ca_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(ca_news.publishedAt.desc())
        default_settings.append(defaults)
    if location == 'nz':
        defaults = nz_news.query.filter(
            and_(nz_news.news_type == news_type, nz_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(nz_news.publishedAt.desc())
        default_settings.append(defaults)
    if location == 'gb':
        defaults = gb_news.query.filter(
            and_(gb_news.news_type == news_type, gb_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(gb_news.publishedAt.desc())
        default_settings.append(defaults)


    return render_template('main/index.html', username=username, user_data=user_data, default_settings=default_settings,
                           news_type=news_type, today=today, location=location)
