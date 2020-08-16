from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint
from datetime import datetime, date, timedelta
import requests
import json
from sqlalchemy import and_
from news.models import za_news
from news.models import us_news
from news.models import au_news
from news.models import ca_news
from news.models import nz_news
from news.models import gb_news

global_search = Blueprint('global_search', __name__)


@global_search.route('/search', methods=['GET', 'POST'])
def search():

    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    country = request.args.get('country')
    news_type = request.args.get('newstype')
    search = request.args.get('search_bar')
    search_everything = request.args.get('search_everything')
    date_category_country = request.args.get('exclude_search_bar')

    try:
        f_from_date = datetime.strptime(from_date, "%Y-%m-%d")
        f_from_full_date = f_from_date.strftime("%d %B, %Y")


        f_to_date = datetime.strptime(to_date, "%Y-%m-%d")
        f_to_full_date = f_to_date.strftime("%d %B, %Y")

        f_year = from_date.split('-')[0]
        f_month = from_date.split('-')[1]
        f_day = from_date.split('-')[2]

        t_year = to_date.split('-')[0]
        t_month = to_date.split('-')[1]
        t_day = to_date.split('-')[2]

        d1 = date(int(f_year), int(f_month), int(f_day))
        d2 = date(int(t_year), int(t_month), int(t_day))

        dd = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]
    except TypeError:
        pass

    # AUSTRALIA

    # No phrase search, AU, Headlines

    if date_category_country == 'on' and country == 'Australia' and news_type == 'Headlines':

        au_headlines = []

        for d in dd:
            headlines = au_news.query.filter(and_(au_news.news_type == 'headlines', au_news.publishedAt.like
            (f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_headlines.append(headlines)

        return render_template('search/au_search.html', news_type=news_type, au_headlines=au_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, AU, Business

    if date_category_country == 'on' and country == 'Australia' and news_type == 'Business':

        au_business = []

        for d in dd:
            business = au_news.query.filter(and_(au_news.news_type == 'business', au_news.publishedAt.like
            (f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_business.append(business)

        return render_template('search/au_search.html', news_type=news_type, au_business=au_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, AU, Technology

    if date_category_country == 'on' and country == 'Australia' and news_type == 'Technology':

        au_technology = []

        for d in dd:
            technology = au_news.query.filter(and_(au_news.news_type == 'technology', au_news.publishedAt.like
            (f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_technology.append(technology)

        return render_template('search/au_search.html', news_type=news_type, au_technology=au_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, AU, Health

    if date_category_country == 'on' and country == 'Australia' and news_type == 'Health':

        au_health = []

        for d in dd:
            health = au_news.query.filter(and_(au_news.news_type == 'health', au_news.publishedAt.like
            (f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_health.append(health)

        return render_template('search/au_search.html', news_type=news_type, au_health=au_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, AU, Science

    if date_category_country == 'on' and country == 'Australia' and news_type == 'Science':

        au_science = []

        for d in dd:
            science = au_news.query.filter(and_(au_news.news_type == 'science', au_news.publishedAt.like
            (f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_science.append(science)

        return render_template('search/au_search.html', news_type=news_type, au_science=au_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, AU, Sport

    if date_category_country == 'on' and country == 'Australia' and news_type == 'Sport':

        au_sport = []

        for d in dd:
            sport = au_news.query.filter(and_(au_news.news_type == 'sports', au_news.publishedAt.like
            (f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_sport.append(sport)

        return render_template('search/au_search.html', news_type=news_type, au_sport=au_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, AU, Entertainment

    if date_category_country == 'on' and country == 'Australia' and news_type == 'Entertainment':

        au_entertainment = []

        for d in dd:
            entertainment = au_news.query.filter(and_(au_news.news_type == 'entertainment', au_news.publishedAt.like
            (f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_entertainment.append(entertainment)

        return render_template('search/au_search.html', news_type=news_type, au_entertainment=au_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, AU, Headlines

    if search != 'None' and country == 'Australia' and news_type == 'Headlines':

        au_search_headlines = []

        for d in dd:
            search_headlines = au_news.query.filter(and_(au_news.news_type == 'headlines',
                                                         au_news.description.contains(search) | au_news.title.contains(search),
                                                         au_news.publishedAt.like(f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_search_headlines.append(search_headlines)

        return render_template('search/au_search.html', news_type=news_type, au_search_headlines=au_search_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, AU, Business

    if search != 'None' and country == 'Australia' and news_type == 'Business':

        au_search_business = []

        for d in dd:
            search_business = au_news.query.filter(and_(au_news.news_type == 'business',
                                                         au_news.description.contains(search) | au_news.title.contains(search),
                                                         au_news.publishedAt.like(f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_search_business.append(search_business)

        return render_template('search/au_search.html', news_type=news_type, au_search_business=au_search_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, AU, Technology

    if search != 'None' and country == 'Australia' and news_type == 'Technology':

        au_search_technology = []

        for d in dd:
            search_technology = au_news.query.filter(and_(au_news.news_type == 'technology',
                                                         au_news.description.contains(search) | au_news.title.contains(search),
                                                         au_news.publishedAt.like(f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_search_technology.append(search_technology)

        return render_template('search/au_search.html', news_type=news_type, au_search_technology=au_search_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, AU, Technology

    if search != 'None' and country == 'Australia' and news_type == 'Health':

        au_search_health = []

        for d in dd:
            search_health = au_news.query.filter(and_(au_news.news_type == 'health',
                                                         au_news.description.contains(search) | au_news.title.contains(search),
                                                         au_news.publishedAt.like(f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_search_health.append(search_health)

        return render_template('search/au_search.html', news_type=news_type, au_search_health=au_search_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, AU, Science

    if search != 'None' and country == 'Australia' and news_type == 'Science':

        au_search_science = []

        for d in dd:
            search_science = au_news.query.filter(and_(au_news.news_type == 'science',
                                                         au_news.description.contains(search) | au_news.title.contains(search),
                                                         au_news.publishedAt.like(f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_search_science.append(search_science)

        return render_template('search/au_search.html', news_type=news_type, au_search_science=au_search_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, AU, Sport

    if search != 'None' and country == 'Australia' and news_type == 'Sport':

        au_search_sport = []

        for d in dd:
            search_sport = au_news.query.filter(and_(au_news.news_type == 'sports',
                                                         au_news.description.contains(search) | au_news.title.contains(search),
                                                         au_news.publishedAt.like(f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_search_sport.append(search_sport)

        return render_template('search/au_search.html', news_type=news_type, au_search_sport=au_search_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, AU, Entertainment

    if search != 'None' and country == 'Australia' and news_type == 'Entertainment':

        au_search_entertainment = []

        for d in dd:
            search_entertainment = au_news.query.filter(and_(au_news.news_type == 'entertainment',
                                                         au_news.description.contains(search) | au_news.title.contains(search),
                                                         au_news.publishedAt.like(f'%{d}%'))).order_by(au_news.publishedAt.desc())

            au_search_entertainment.append(search_entertainment)

        return render_template('search/au_search.html', news_type=news_type, au_search_entertainment=au_search_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)




    # CANADA

    # No phrase search, CA, Headlines

    if date_category_country == 'on' and country == 'Canada' and news_type == 'Headlines':

        ca_headlines = []

        for d in dd:
            headlines = ca_news.query.filter(and_(ca_news.news_type == 'headlines', ca_news.publishedAt.like
            (f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_headlines.append(headlines)

        return render_template('search/ca_search.html', news_type=news_type, ca_headlines=ca_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, CA, Business

    if date_category_country == 'on' and country == 'Canada' and news_type == 'Business':

        ca_business = []

        for d in dd:
            business = ca_news.query.filter(and_(ca_news.news_type == 'business', ca_news.publishedAt.like
            (f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_business.append(business)

        return render_template('search/ca_search.html', news_type=news_type, ca_business=ca_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, CA, Technology

    if date_category_country == 'on' and country == 'Canada' and news_type == 'Technology':

        ca_technology = []

        for d in dd:
            technology = ca_news.query.filter(and_(ca_news.news_type == 'technology', ca_news.publishedAt.like
            (f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_technology.append(technology)

        return render_template('search/ca_search.html', news_type=news_type, ca_technology=ca_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, CA, Health

    if date_category_country == 'on' and country == 'Canada' and news_type == 'Health':

        ca_health = []

        for d in dd:
            health = ca_news.query.filter(and_(ca_news.news_type == 'health', ca_news.publishedAt.like
            (f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_health.append(health)

        return render_template('search/ca_search.html', news_type=news_type, ca_health=ca_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, CA, Science

    if date_category_country == 'on' and country == 'Canada' and news_type == 'Science':

        ca_science = []

        for d in dd:
            science = ca_news.query.filter(and_(ca_news.news_type == 'science', ca_news.publishedAt.like
            (f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_science.append(science)

        return render_template('search/ca_search.html', news_type=news_type, ca_science=ca_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, CA, Sport

    if date_category_country == 'on' and country == 'Canada' and news_type == 'Sport':

        ca_sport = []

        for d in dd:
            sport = ca_news.query.filter(and_(ca_news.news_type == 'sports', ca_news.publishedAt.like
            (f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_sport.append(sport)

        return render_template('search/ca_search.html', news_type=news_type, ca_sport=ca_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, CA, Entertainment

    if date_category_country == 'on' and country == 'Canada' and news_type == 'Entertainment':

        ca_entertainment = []

        for d in dd:
            entertainment = ca_news.query.filter(and_(ca_news.news_type == 'entertainment', ca_news.publishedAt.like
            (f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_entertainment.append(entertainment)

        return render_template('search/ca_search.html', news_type=news_type, ca_entertainment=ca_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, CA, Headlines

    if search != 'None' and country == 'Canada' and news_type == 'Headlines':

        ca_search_headlines = []

        for d in dd:
            search_headlines = ca_news.query.filter(and_(ca_news.news_type == 'headlines',
                                                         ca_news.description.contains(search) | ca_news.title.contains(search),
                                                         ca_news.publishedAt.like(f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_search_headlines.append(search_headlines)

        return render_template('search/ca_search.html', news_type=news_type, ca_search_headlines=ca_search_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, CA, Business

    if search != 'None' and country == 'Canada' and news_type == 'Business':

        ca_search_business = []

        for d in dd:
            search_business = ca_news.query.filter(and_(ca_news.news_type == 'business',
                                                        ca_news.description.contains(search) | ca_news.title.contains(search),
                                                        ca_news.publishedAt.like(f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_search_business.append(search_business)

        return render_template('search/ca_search.html', news_type=news_type, ca_search_business=ca_search_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, CA, Technology

    if search != 'None' and country == 'Canada' and news_type == 'Technology':

        ca_search_technology = []

        for d in dd:
            search_technology = ca_news.query.filter(and_(ca_news.news_type == 'technology',
                                                          ca_news.description.contains(search) | ca_news.title.contains(search),
                                                          ca_news.publishedAt.like(f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_search_technology.append(search_technology)

        return render_template('search/ca_search.html', news_type=news_type, ca_search_technology=ca_search_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, CA, Health

    if search != 'None' and country == 'Canada' and news_type == 'Health':

        ca_search_health = []

        for d in dd:
            search_health = ca_news.query.filter(and_(ca_news.news_type == 'health',
                                                      ca_news.description.contains(search) | ca_news.title.contains(search),
                                                      ca_news.publishedAt.like(f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_search_health.append(search_health)

        return render_template('search/ca_search.html', news_type=news_type, ca_search_health=ca_search_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, CA, Science

    if search != 'None' and country == 'Canada' and news_type == 'Science':

        ca_search_science = []

        for d in dd:
            search_science = ca_news.query.filter(and_(ca_news.news_type == 'science',
                                                       ca_news.description.contains(search) | ca_news.title.contains(search),
                                                       ca_news.publishedAt.like(f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_search_science.append(search_science)

        return render_template('search/ca_search.html', news_type=news_type, ca_search_science=ca_search_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, CA, Sport

    if search != 'None' and country == 'Canada' and news_type == 'Sport':

        ca_search_sport = []

        for d in dd:
            search_sport = ca_news.query.filter(and_(ca_news.news_type == 'sports',
                                                     ca_news.description.contains(search) | ca_news.title.contains(search),
                                                     ca_news.publishedAt.like(f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_search_sport.append(search_sport)

        return render_template('search/ca_search.html', news_type=news_type, ca_search_sport=ca_search_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, CA, Entertainment

    if search != 'None' and country == 'Canada' and news_type == 'Entertainment':

        ca_search_entertainment = []

        for d in dd:
            search_entertainment = ca_news.query.filter(and_(ca_news.news_type == 'entertainment',
                                                             ca_news.description.contains(search) | ca_news.title.contains(search),
                                                             ca_news.publishedAt.like(f'%{d}%'))).order_by(ca_news.publishedAt.desc())

            ca_search_entertainment.append(search_entertainment)

        return render_template('search/ca_search.html', news_type=news_type, ca_search_entertainment=ca_search_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)





    # GREAT BRITAIN

    # No phrase search, GB, Headlines

    if date_category_country == 'on' and country == 'Great Britain' and news_type == 'Headlines':

        gb_headlines = []

        for d in dd:
            headlines = gb_news.query.filter(and_(gb_news.news_type == 'headlines', gb_news.publishedAt.like
            (f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_headlines.append(headlines)

        return render_template('search/gb_search.html', news_type=news_type, gb_headlines=gb_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, GB, Business

    if date_category_country == 'on' and country == 'Great Britain' and news_type == 'Business':

        gb_business = []

        for d in dd:
            business = gb_news.query.filter(and_(gb_news.news_type == 'business', gb_news.publishedAt.like
            (f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_business.append(business)

        return render_template('search/gb_search.html', news_type=news_type, gb_business=gb_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, GB, Technology

    if date_category_country == 'on' and country == 'Great Britain' and news_type == 'Technology':

        gb_technology = []

        for d in dd:
            technology = gb_news.query.filter(and_(gb_news.news_type == 'technology', gb_news.publishedAt.like
            (f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_technology.append(technology)

        return render_template('search/gb_search.html', news_type=news_type, gb_technology=gb_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, GB, Health

    if date_category_country == 'on' and country == 'Great Britain' and news_type == 'Health':

        gb_health = []

        for d in dd:
            health = gb_news.query.filter(and_(gb_news.news_type == 'health', gb_news.publishedAt.like
            (f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_health.append(health)

        return render_template('search/gb_search.html', news_type=news_type, gb_health=gb_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, GB, Science

    if date_category_country == 'on' and country == 'Great Britain' and news_type == 'Science':

        gb_science = []

        for d in dd:
            science = gb_news.query.filter(and_(gb_news.news_type == 'science', gb_news.publishedAt.like
            (f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_science.append(science)

        return render_template('search/gb_search.html', news_type=news_type, gb_science=gb_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, GB, Sport

    if date_category_country == 'on' and country == 'Great Britain' and news_type == 'Sport':

        gb_sport = []

        for d in dd:
            sport = gb_news.query.filter(and_(gb_news.news_type == 'sports', gb_news.publishedAt.like
            (f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_sport.append(sport)

        return render_template('search/gb_search.html', news_type=news_type, gb_sport=gb_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, GB, Entertainment

    if date_category_country == 'on' and country == 'Great Britain' and news_type == 'Entertainment':

        gb_entertainment = []

        for d in dd:
            entertainment = gb_news.query.filter(and_(gb_news.news_type == 'entertainment', gb_news.publishedAt.like
            (f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_entertainment.append(entertainment)

        return render_template('search/gb_search.html', news_type=news_type, gb_entertainment=gb_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, GB, Headlines

    if search != 'None' and country == 'Great Britain' and news_type == 'Headlines':

        gb_search_headlines = []

        for d in dd:
            search_headlines = gb_news.query.filter(and_(gb_news.news_type == 'headlines',
                                                         gb_news.description.contains(search) | gb_news.title.contains(search),
                                                         gb_news.publishedAt.like(f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_search_headlines.append(search_headlines)

        return render_template('search/gb_search.html', news_type=news_type, gb_search_headlines=gb_search_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, GB, Business

    if search != 'None' and country == 'Great Britain' and news_type == 'Business':

        gb_search_business = []

        for d in dd:
            search_business = gb_news.query.filter(and_(gb_news.news_type == 'business',
                                                        gb_news.description.contains(search) | gb_news.title.contains(search),
                                                        gb_news.publishedAt.like(f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_search_business.append(search_business)

        return render_template('search/gb_search.html', news_type=news_type, gb_search_business=gb_search_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, GB, Technology

    if search != 'None' and country == 'Great Britain' and news_type == 'Technology':

        gb_search_technology = []

        for d in dd:
            search_technology = gb_news.query.filter(and_(gb_news.news_type == 'technology',
                                                          gb_news.description.contains(search) | gb_news.title.contains(search),
                                                          gb_news.publishedAt.like(f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_search_technology.append(search_technology)

        return render_template('search/gb_search.html', news_type=news_type, gb_search_technology=gb_search_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, GB, Health

    if search != 'None' and country == 'Great Britain' and news_type == 'Health':

        gb_search_health = []

        for d in dd:
            search_health = gb_news.query.filter(and_(gb_news.news_type == 'health',
                                                      gb_news.description.contains(search) | gb_news.title.contains(search),
                                                      gb_news.publishedAt.like(f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_search_health.append(search_health)

        return render_template('search/gb_search.html', news_type=news_type, gb_search_health=gb_search_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, GB, Science

    if search != 'None' and country == 'Great Britain' and news_type == 'Science':

        gb_search_science = []

        for d in dd:
            search_science = gb_news.query.filter(and_(gb_news.news_type == 'science',
                                                       gb_news.description.contains(search) | gb_news.title.contains(search),
                                                       gb_news.publishedAt.like(f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_search_science.append(search_science)

        return render_template('search/gb_search.html', news_type=news_type, gb_search_science=gb_search_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, GB, Sport

    if search != 'None' and country == 'Great Britain' and news_type == 'Sport':

        gb_search_sport = []

        for d in dd:
            search_sport = gb_news.query.filter(and_(gb_news.news_type == 'sports',
                                                     gb_news.description.contains(search) | gb_news.title.contains(search),
                                                     gb_news.publishedAt.like(f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_search_sport.append(search_sport)

        return render_template('search/gb_search.html', news_type=news_type, gb_search_sport=gb_search_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, GB, Entertainment

    if search != 'None' and country == 'Great Britain' and news_type == 'Entertainment':

        gb_search_entertainment = []

        for d in dd:
            search_entertainment = gb_news.query.filter(and_(gb_news.news_type == 'entertainment',
                                                             gb_news.description.contains(search) | gb_news.title.contains(search),
                                                             gb_news.publishedAt.like(f'%{d}%'))).order_by(gb_news.publishedAt.desc())

            gb_search_entertainment.append(search_entertainment)

        return render_template('search/gb_search.html', news_type=news_type, gb_search_entertainment=gb_search_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)





    # NEW ZEALAND

    # No phrase search, NZ, Headlines

    if date_category_country == 'on' and country == 'New Zealand' and news_type == 'Headlines':

        nz_headlines = []

        for d in dd:
            headlines = nz_news.query.filter(and_(nz_news.news_type == 'headlines', nz_news.publishedAt.like
            (f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_headlines.append(headlines)

        return render_template('search/nz_search.html', news_type=news_type, nz_headlines=nz_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, NZ, Business

    if date_category_country == 'on' and country == 'New Zealand' and news_type == 'Business':

        nz_business = []

        for d in dd:
            business = nz_news.query.filter(and_(nz_news.news_type == 'business', nz_news.publishedAt.like
            (f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_business.append(business)

        return render_template('search/nz_search.html', news_type=news_type, nz_business=nz_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, NZ, Technology

    if date_category_country == 'on' and country == 'New Zealand' and news_type == 'Technology':

        nz_technology = []

        for d in dd:
            technology = nz_news.query.filter(and_(nz_news.news_type == 'technology', nz_news.publishedAt.like
            (f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_technology.append(technology)

        return render_template('search/nz_search.html', news_type=news_type, nz_technology=nz_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, NZ, Health

    if date_category_country == 'on' and country == 'New Zealand' and news_type == 'Health':

        nz_health = []

        for d in dd:
            health = nz_news.query.filter(and_(nz_news.news_type == 'health', nz_news.publishedAt.like
            (f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_health.append(health)

        return render_template('search/nz_search.html', news_type=news_type, nz_health=nz_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, NZ, Science

    if date_category_country == 'on' and country == 'New Zealand' and news_type == 'Science':

        nz_science = []

        for d in dd:
            science = nz_news.query.filter(and_(nz_news.news_type == 'science', nz_news.publishedAt.like
            (f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_science.append(science)

        return render_template('search/nz_search.html', news_type=news_type, nz_science=nz_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, NZ, Sport

    if date_category_country == 'on' and country == 'New Zealand' and news_type == 'Sport':

        nz_sport = []

        for d in dd:
            sport = nz_news.query.filter(and_(nz_news.news_type == 'sports', nz_news.publishedAt.like
            (f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_sport.append(sport)

        return render_template('search/nz_search.html', news_type=news_type, nz_sport=nz_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, NZ, Entertainment

    if date_category_country == 'on' and country == 'New Zealand' and news_type == 'Entertainment':

        nz_entertainment = []

        for d in dd:
            entertainment = nz_news.query.filter(and_(nz_news.news_type == 'entertainment', nz_news.publishedAt.like
            (f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_entertainment.append(entertainment)

        return render_template('search/nz_search.html', news_type=news_type, nz_entertainment=nz_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, NZ, Headlines

    if search != 'None' and country == 'New Zealand' and news_type == 'Headlines':

        nz_search_headlines = []

        for d in dd:
            search_headlines = nz_news.query.filter(and_(nz_news.news_type == 'headlines',
                                                         nz_news.description.contains(search) | nz_news.title.contains(search),
                                                         nz_news.publishedAt.like(f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_search_headlines.append(search_headlines)

        return render_template('search/nz_search.html', news_type=news_type, nz_search_headlines=nz_search_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, NZ, Business

    if search != 'None' and country == 'New Zealand' and news_type == 'Business':

        nz_search_business = []

        for d in dd:
            search_business = nz_news.query.filter(and_(nz_news.news_type == 'business',
                                                        nz_news.description.contains(search) | nz_news.title.contains(search),
                                                        nz_news.publishedAt.like(f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_search_business.append(search_business)

        return render_template('search/nz_search.html', news_type=news_type, nz_search_business=nz_search_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, NZ, Technology

    if search != 'None' and country == 'New Zealand' and news_type == 'Technology':

        nz_search_technology = []

        for d in dd:
            search_technology = nz_news.query.filter(and_(nz_news.news_type == 'technology',
                                                          nz_news.description.contains(search) | nz_news.title.contains(search),
                                                          nz_news.publishedAt.like(f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_search_technology.append(search_technology)

        return render_template('search/nz_search.html', news_type=news_type, nz_search_technology=nz_search_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, NZ, Health

    if search != 'None' and country == 'New Zealand' and news_type == 'Health':

        nz_search_health = []

        for d in dd:
            search_health = nz_news.query.filter(and_(nz_news.news_type == 'health',
                                                      nz_news.description.contains(search) | nz_news.title.contains(search),
                                                      nz_news.publishedAt.like(f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_search_health.append(search_health)

        return render_template('search/nz_search.html', news_type=news_type, nz_search_health=nz_search_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, NZ, Science

    if search != 'None' and country == 'New Zealand' and news_type == 'Science':

        nz_search_science = []

        for d in dd:
            search_science = nz_news.query.filter(and_(nz_news.news_type == 'science',
                                                       nz_news.description.contains(search) | nz_news.title.contains(search),
                                                       nz_news.publishedAt.like(f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_search_science.append(search_science)

        return render_template('search/nz_search.html', news_type=news_type, nz_search_science=nz_search_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, NZ, Sport

    if search != 'None' and country == 'New Zealand' and news_type == 'Sport':

        nz_search_sport = []

        for d in dd:
            search_sport = nz_news.query.filter(and_(nz_news.news_type == 'sports',
                                                     nz_news.description.contains(search) | nz_news.title.contains(search),
                                                     nz_news.publishedAt.like(f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_search_sport.append(search_sport)

        return render_template('search/nz_search.html', news_type=news_type, nz_search_sport=nz_search_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, NZ, Entertainment

    if search != 'None' and country == 'New Zealand' and news_type == 'Entertainment':

        nz_search_entertainment = []

        for d in dd:
            search_entertainment = nz_news.query.filter(and_(nz_news.news_type == 'entertainment',
                                                             nz_news.description.contains(search) | nz_news.title.contains(search),
                                                             nz_news.publishedAt.like(f'%{d}%'))).order_by(nz_news.publishedAt.desc())

            nz_search_entertainment.append(search_entertainment)

        return render_template('search/nz_search.html', news_type=news_type, nz_search_entertainment=nz_search_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)




    # SOUTH AFRICA

    # No phrase search, ZA, Headlines

    if date_category_country == 'on' and country == 'South Africa' and news_type == 'Headlines':

        za_headlines = []

        for d in dd:
            headlines = za_news.query.filter(and_(za_news.news_type == 'headlines', za_news.publishedAt.like
            (f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_headlines.append(headlines)

        return render_template('search/za_search.html', news_type=news_type, za_headlines=za_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, ZA, Business

    if date_category_country == 'on' and country == 'South Africa' and news_type == 'Business':

        za_business = []

        for d in dd:
            business = za_news.query.filter(and_(za_news.news_type == 'business', za_news.publishedAt.like
            (f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_business.append(business)

        return render_template('search/za_search.html', news_type=news_type, za_business=za_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, ZA, Technology

    if date_category_country == 'on' and country == 'South Africa' and news_type == 'Technology':

        za_technology = []

        for d in dd:
            technology = za_news.query.filter(and_(za_news.news_type == 'technology', za_news.publishedAt.like
            (f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_technology.append(technology)

        return render_template('search/za_search.html', news_type=news_type, za_technology=za_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, ZA, Health

    if date_category_country == 'on' and country == 'South Africa' and news_type == 'Health':

        za_health = []

        for d in dd:
            health = za_news.query.filter(and_(za_news.news_type == 'health', za_news.publishedAt.like
            (f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_health.append(health)

        return render_template('search/za_search.html', news_type=news_type, za_health=za_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, ZA, Science

    if date_category_country == 'on' and country == 'South Africa' and news_type == 'Science':

        za_science = []

        for d in dd:
            science = za_news.query.filter(and_(za_news.news_type == 'science', za_news.publishedAt.like
            (f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_science.append(science)

        return render_template('search/za_search.html', news_type=news_type, za_science=za_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, ZA, Sport

    if date_category_country == 'on' and country == 'South Africa' and news_type == 'Sport':

        za_sport = []

        for d in dd:
            sport = za_news.query.filter(and_(za_news.news_type == 'sports', za_news.publishedAt.like
            (f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_sport.append(sport)

        return render_template('search/za_search.html', news_type=news_type, za_sport=za_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, ZA, Entertainment

    if date_category_country == 'on' and country == 'South Africa' and news_type == 'Entertainment':

        za_entertainment = []

        for d in dd:
            entertainment = za_news.query.filter(and_(za_news.news_type == 'entertainment', za_news.publishedAt.like
            (f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_entertainment.append(entertainment)

        return render_template('search/za_search.html', news_type=news_type, za_entertainment=za_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, ZA, Headlines

    if search != 'None' and country == 'South Africa' and news_type == 'Headlines':

        za_search_headlines = []

        for d in dd:
            search_headlines = za_news.query.filter(and_(za_news.news_type == 'headlines',
                                                         za_news.description.contains(search) | za_news.title.contains(search),
                                                         za_news.publishedAt.like(f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_search_headlines.append(search_headlines)

        return render_template('search/za_search.html', news_type=news_type, za_search_headlines=za_search_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, ZA, Business

    if search != 'None' and country == 'South Africa' and news_type == 'Business':

        za_search_business = []

        for d in dd:
            search_business = za_news.query.filter(and_(za_news.news_type == 'business',
                                                        za_news.description.contains(search) | za_news.title.contains(search),
                                                        za_news.publishedAt.like(f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_search_business.append(search_business)

        return render_template('search/za_search.html', news_type=news_type, za_search_business=za_search_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, ZA, Technology

    if search != 'None' and country == 'South Africa' and news_type == 'Technology':

        za_search_technology = []

        for d in dd:
            search_technology = za_news.query.filter(and_(za_news.news_type == 'technology',
                                                          za_news.description.contains(search) | za_news.title.contains(search),
                                                          za_news.publishedAt.like(f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_search_technology.append(search_technology)

        return render_template('search/za_search.html', news_type=news_type, za_search_technology=za_search_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, ZA, Health

    if search != 'None' and country == 'South Africa' and news_type == 'Health':

        za_search_health = []

        for d in dd:
            search_health = za_news.query.filter(and_(za_news.news_type == 'health',
                                                      za_news.description.contains(search) | za_news.title.contains(search),
                                                      za_news.publishedAt.like(f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_search_health.append(search_health)

        return render_template('search/za_search.html', news_type=news_type, za_search_health=za_search_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, ZA, Science

    if search != 'None' and country == 'South Africa' and news_type == 'Science':

        za_search_science = []

        for d in dd:
            search_science = za_news.query.filter(and_(za_news.news_type == 'science',
                                                       za_news.description.contains(search) | za_news.title.contains(search),
                                                       za_news.publishedAt.like(f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_search_science.append(search_science)

        return render_template('search/za_search.html', news_type=news_type, za_search_science=za_search_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, ZA, Sport

    if search != 'None' and country == 'South Africa' and news_type == 'Sport':

        za_search_sport = []

        for d in dd:
            search_sport = za_news.query.filter(and_(za_news.news_type == 'sports',
                                                     za_news.description.contains(search) | za_news.title.contains(search),
                                                     za_news.publishedAt.like(f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_search_sport.append(search_sport)

        return render_template('search/za_search.html', news_type=news_type, za_search_sport=za_search_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, ZA, Entertainment

    if search != 'None' and country == 'South Africa' and news_type == 'Entertainment':

        za_search_entertainment = []

        for d in dd:
            search_entertainment = za_news.query.filter(and_(za_news.news_type == 'entertainment',
                                                             za_news.description.contains(search) | za_news.title.contains(search),
                                                             za_news.publishedAt.like(f'%{d}%'))).order_by(za_news.publishedAt.desc())

            za_search_entertainment.append(search_entertainment)

        return render_template('search/za_search.html', news_type=news_type, za_search_entertainment=za_search_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)





    # UNITED STATES

    # No phrase search, US, Headlines

    if date_category_country == 'on' and country == 'United States' and news_type == 'Headlines':

        us_headlines = []

        for d in dd:
            headlines = us_news.query.filter(and_(us_news.news_type == 'headlines', us_news.publishedAt.like
            (f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_headlines.append(headlines)

        return render_template('search/us_search.html', news_type=news_type, us_headlines=us_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, US, Business

    if date_category_country == 'on' and country == 'United States' and news_type == 'Business':

        us_business = []

        for d in dd:
            business = us_news.query.filter(and_(us_news.news_type == 'business', us_news.publishedAt.like
            (f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_business.append(business)

        return render_template('search/us_search.html', news_type=news_type, us_business=us_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, US, Technology

    if date_category_country == 'on' and country == 'United States' and news_type == 'Technology':

        us_technology = []

        for d in dd:
            technology = us_news.query.filter(and_(us_news.news_type == 'technology', us_news.publishedAt.like
            (f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_technology.append(technology)

        return render_template('search/us_search.html', news_type=news_type, us_technology=us_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, US, Health

    if date_category_country == 'on' and country == 'United States' and news_type == 'Health':

        us_health = []

        for d in dd:
            health = us_news.query.filter(and_(us_news.news_type == 'health', us_news.publishedAt.like
            (f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_health.append(health)

        return render_template('search/us_search.html', news_type=news_type, us_health=us_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, US, Science

    if date_category_country == 'on' and country == 'United States' and news_type == 'Science':

        us_science = []

        for d in dd:
            science = us_news.query.filter(and_(us_news.news_type == 'science', us_news.publishedAt.like
            (f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_science.append(science)

        return render_template('search/us_search.html', news_type=news_type, us_science=us_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, US, Sport

    if date_category_country == 'on' and country == 'United States' and news_type == 'Sport':

        us_sport = []

        for d in dd:
            sport = us_news.query.filter(and_(us_news.news_type == 'sports', us_news.publishedAt.like
            (f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_sport.append(sport)

        return render_template('search/us_search.html', news_type=news_type, us_sport=us_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # No phrase search, US, Entertainment

    if date_category_country == 'on' and country == 'United States' and news_type == 'Entertainment':

        us_entertainment = []

        for d in dd:
            entertainment = us_news.query.filter(and_(us_news.news_type == 'entertainment', us_news.publishedAt.like
            (f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_entertainment.append(entertainment)

        return render_template('search/us_search.html', news_type=news_type, us_entertainment=us_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, US, Headlines

    if search != 'None' and country == 'United States' and news_type == 'Headlines':

        us_search_headlines = []

        for d in dd:
            search_headlines = us_news.query.filter(and_(us_news.news_type == 'headlines',
                                                         us_news.description.contains(search) | us_news.title.contains(search),
                                                         us_news.publishedAt.like(f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_search_headlines.append(search_headlines)

        return render_template('search/us_search.html', news_type=news_type, us_search_headlines=us_search_headlines, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, US, Business

    if search != 'None' and country == 'United States' and news_type == 'Business':

        us_search_business = []

        for d in dd:
            search_business = us_news.query.filter(and_(us_news.news_type == 'business',
                                                        us_news.description.contains(search) | us_news.title.contains(search),
                                                        us_news.publishedAt.like(f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_search_business.append(search_business)

        return render_template('search/us_search.html', news_type=news_type, us_search_business=us_search_business, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, US, Technology

    if search != 'None' and country == 'United States' and news_type == 'Technology':

        us_search_technology = []

        for d in dd:
            search_technology = us_news.query.filter(and_(us_news.news_type == 'technology',
                                                          us_news.description.contains(search) | us_news.title.contains(search),
                                                          us_news.publishedAt.like(f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_search_technology.append(search_technology)

        return render_template('search/us_search.html', news_type=news_type, us_search_technology=us_search_technology, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, US, Health

    if search != 'None' and country == 'United States' and news_type == 'Health':

        us_search_health = []

        for d in dd:
            search_health = us_news.query.filter(and_(us_news.news_type == 'health',
                                                      us_news.description.contains(search) | us_news.title.contains(search),
                                                      us_news.publishedAt.like(f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_search_health.append(search_health)

        return render_template('search/us_search.html', news_type=news_type, us_search_health=us_search_health, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, US, Science

    if search != 'None' and country == 'United States' and news_type == 'Science':

        us_search_science = []

        for d in dd:
            search_science = us_news.query.filter(and_(us_news.news_type == 'science',
                                                       us_news.description.contains(search) | us_news.title.contains(search),
                                                       us_news.publishedAt.like(f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_search_science.append(search_science)

        return render_template('search/us_search.html', news_type=news_type, us_search_science=us_search_science, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, US, Sport

    if search != 'None' and country == 'United States' and news_type == 'Sport':

        us_search_sport = []

        for d in dd:
            search_sport = us_news.query.filter(and_(us_news.news_type == 'sports',
                                                     us_news.description.contains(search) | us_news.title.contains(search),
                                                     us_news.publishedAt.like(f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_search_sport.append(search_sport)

        return render_template('search/us_search.html', news_type=news_type, us_search_sport=us_search_sport, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)

    # Phrase search, US, Entertainment

    if search != 'None' and country == 'United States' and news_type == 'Entertainment':

        us_search_entertainment = []

        for d in dd:
            search_entertainment = us_news.query.filter(and_(us_news.news_type == 'entertainment',
                                                             us_news.description.contains(search) | us_news.title.contains(search),
                                                             us_news.publishedAt.like(f'%{d}%'))).order_by(us_news.publishedAt.desc())

            us_search_entertainment.append(search_entertainment)

        return render_template('search/us_search.html', news_type=news_type, us_search_entertainment=us_search_entertainment, country=country,
                               from_date=f_from_full_date, to_date=f_to_full_date, search=search)


    # Phrase search, Everything

    if search_everything == 'on' and date_category_country != 'on':

        everything_search = []

        au_search_everything = au_news.query.filter(and_(au_news.description.contains(search) | au_news.title.contains(search))).order_by(au_news.publishedAt.desc())

        everything_search.append(au_search_everything)

        ca_search_everything = ca_news.query.filter(and_(ca_news.description.contains(search) | ca_news.title.contains(search))).order_by(ca_news.publishedAt.desc())

        everything_search.append(ca_search_everything)

        gb_search_everything = gb_news.query.filter(and_(gb_news.description.contains(search) | gb_news.title.contains(search))).order_by(gb_news.publishedAt.desc())

        everything_search.append(gb_search_everything)

        nz_search_everything = nz_news.query.filter(and_(nz_news.description.contains(search) | nz_news.title.contains(search))).order_by(nz_news.publishedAt.desc())

        everything_search.append(nz_search_everything)

        za_search_everything = za_news.query.filter(and_(za_news.description.contains(search) | za_news.title.contains(search))).order_by(za_news.publishedAt.desc())

        everything_search.append(za_search_everything)

        us_search_everything = us_news.query.filter(and_(us_news.description.contains(search) | us_news.title.contains(search))).order_by(us_news.publishedAt.desc())

        everything_search.append(us_search_everything)

        return render_template('search/everything_search.html', news_type=news_type, everything_search=everything_search, country=country,
                               search_everything=search_everything, date_category_country=date_category_country, search=search)


    # Both Check Boxes Error

    if date_category_country == 'on' and search_everything == 'on':

        flash('message')

        return render_template('search/everything_search.html')


# def strftime(date, format):
#     date = x.publishedAt.replace('T', " ").replace('Z', "")
#     date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
#     return date.strftime("%m/%d/%Y")

# global_search.jinja_env.filters['strtime'] = strftime

@global_search.route('/all_search', methods=['GET', 'POST'])
def all_search():

    search = request.args.get('search_item')

    everything_search = []

    au_search_everything = au_news.query.filter(and_(au_news.description.contains(search) | au_news.title.contains(search))).order_by(au_news.publishedAt.desc())

    everything_search.append(au_search_everything)

    ca_search_everything = ca_news.query.filter(and_(ca_news.description.contains(search) | ca_news.title.contains(search))).order_by(ca_news.publishedAt.desc())

    everything_search.append(ca_search_everything)

    gb_search_everything = gb_news.query.filter(and_(gb_news.description.contains(search) | gb_news.title.contains(search))).order_by(gb_news.publishedAt.desc())

    everything_search.append(gb_search_everything)

    nz_search_everything = nz_news.query.filter(and_(nz_news.description.contains(search) | nz_news.title.contains(search))).order_by(nz_news.publishedAt.desc())

    everything_search.append(nz_search_everything)

    za_search_everything = za_news.query.filter(and_(za_news.description.contains(search) | za_news.title.contains(search))).order_by(za_news.publishedAt.desc())

    everything_search.append(za_search_everything)

    us_search_everything = us_news.query.filter(and_(us_news.description.contains(search) | us_news.title.contains(search))).order_by(us_news.publishedAt.desc())

    everything_search.append(us_search_everything)

    # for i in everything_search:
    #     for x in i:
    #         date = x.publishedAt.replace('T', " ").replace('Z', "")
    #         date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    #         date = date.strftime("%m/%d/%Y")

    # for i in everything_search:
    #     for x in i:
    #         c = x.location
    #         print(c)

    return render_template('search/everything_search.html', everything_search=everything_search, search=search)

    #news_type=news_type, everything_search=everything_search, country=country,
    #                           search_everything=search_everything, date_category_country=date_category_country, search=search

