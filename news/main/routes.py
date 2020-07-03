from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from flask_user import login_required
from flask_login import current_user
from datetime import datetime
from sqlalchemy import and_, tuple_, update
from news import db
from news.models import za_news
from news.models import us_news
from news.models import au_news
from news.models import ca_news
from news.models import nz_news
from news.models import gb_news
from news.models import User
import json
import codecs
import hmac

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
    print(location)

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]
    news_type = user_defaults[1]
    if news_type == None:
        news_type = user_defaults[1]
    else:
        news_type = user_defaults[1].lower()

    default_settings = []
    if location == "United States":
        defaults = us_news.query.filter(
            and_(us_news.news_type == news_type, us_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(us_news.publishedAt.desc())
        default_settings.append(defaults)
        location = 'us'
    if location == 'South Africa':
        defaults = za_news.query.filter(
            and_(za_news.news_type == news_type, za_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(za_news.publishedAt.desc())
        default_settings.append(defaults)
        location = 'za'
    if location == 'Australia':
        defaults = au_news.query.filter(
            and_(au_news.news_type == news_type, au_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(au_news.publishedAt.desc())
        default_settings.append(defaults)
        location = 'au'
    if location == 'Canada':
        defaults = ca_news.query.filter(
            and_(ca_news.news_type == news_type, ca_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(ca_news.publishedAt.desc())
        default_settings.append(defaults)
        location = 'ca'
    if location == 'New Zealand':
        defaults = nz_news.query.filter(
            and_(nz_news.news_type == news_type, nz_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(nz_news.publishedAt.desc())
        default_settings.append(defaults)
        location = 'nz'
    if location == 'Great Britain':
        defaults = gb_news.query.filter(
            and_(gb_news.news_type == news_type, gb_news.publishedAt.like(f'%{today_date}%'))) \
            .order_by(gb_news.publishedAt.desc())
        default_settings.append(defaults)
        location = 'gb'


    return render_template('main/index.html', username=username, user_data=user_data, default_settings=default_settings,
                           news_type=news_type, today=today, location=location)

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    today = datetime.now().strftime("%d %B, %Y")
    username = current_user.username
    user_data = User.query.filter(
    and_(User.username == username)
    )

    return render_template('main/profile.html', today=today, username=username, user_data=user_data)


@main.route('/comments', methods=['GET', 'POST'])
@login_required
def comments():

    today = datetime.now().strftime("%d %B, %Y")
    news_id = request.args.get('news_id')
    location = request.args.get('location')
    news_type = request.args.get('newstype')

    if location == 'au':
        article = au_news.query.filter(
            and_(au_news.id == news_id)
        )

        return render_template('main/comments.html', today=today, article=article, news_type=news_type, news_id=news_id)

    elif location == 'ca':
        article = ca_news.query.filter(
            and_(ca_news.id == news_id)
        )

        return render_template('main/comments.html', today=today, article=article, news_type=news_type, news_id=news_id)

    elif location == 'gb':
        article = gb_news.query.filter(
            and_(gb_news.id == news_id)
        )

        return render_template('main/comments.html', today=today, article=article, news_type=news_type, news_id=news_id)

    elif location == 'nz':
        article = nz_news.query.filter(
            and_(nz_news.id == news_id)
        )

        return render_template('main/comments.html', today=today, article=article, news_type=news_type, news_id=news_id)

    elif location == 'za':
        article = za_news.query.filter(
            and_(za_news.id == news_id)
        )

        return render_template('main/comments.html', today=today, article=article, news_type=news_type, news_id=news_id)

    elif location == 'us':
        article = us_news.query.filter(
            and_(us_news.id == news_id)
        )

        return render_template('main/comments.html', today=today, article=article, news_type=news_type, news_id=news_id)


@main.route('/fav_updates', methods=['GET', 'POST'])
@login_required
def fav_updates():

    username = current_user.username
    uname = request.args.get('uname')
    news_type = request.args.get('news_type')
    country = request.args.get('country')

    if news_type == 'None' and country == 'None':
        update = User.query.filter_by(username=username).first()
        update.username = uname
        db.session.commit()

        return redirect(url_for('main.profile'))
    else:
        update = User.query.filter_by(username=username).first()
        update.pref_location = country
        update.pref_news_type = news_type
        update.username = uname
        db.session.commit()

        return redirect(url_for('main.profile'))


@main.route('/sso/', methods=['GET', 'POST'])
@login_required
def sso():


    secret = "753949c5067d66f7de309fa2ccba0b64ff7bbf9b5d8f72185110b532727f828f"
    decode_hex = codecs.getdecoder("hex_codec")
    secret_key = decode_hex(secret)[0]
    print(secret_key)

    token = request.args.get('token')
    h_mac = request.args.get('hmac')
    h_mac = decode_hex(h_mac)[0]
    
    #print(h_mac)
    #h_mac = codecs.getencoder(request.args.get('hmac'))
    #print(token)

    email = "mike.hyland@theworldoftheweb.net"
    name =  "Mike Hyland"
    link = "https://theworldoftheweb.net"
    photo = "https://i.imgur.com/XPAMYQN.jpg"


    payload_dict = {
        "token": token,
        "email": email,
        "name":  name,
        "link":  link,
        "photo": photo
      }

    payload_json = json.dumps(payload_dict)
    print(payload_json)

    h_mac = codecs.encode(hmac.new(payload_json, secret_key))
    payload_hex = codecs.encode(payload_json)


    return redirect(url_for("http://localhost:5100/api/oauth/sso/callback?payload=" + payload_hex + "&hmac=" + h_mac))
    #return redirect(url_for("http://localhost:5100/api/oauth/sso/callback?payload=PAYLOAD&hmac=hmac"))

