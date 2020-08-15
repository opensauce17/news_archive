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
from elasticsearch import Elasticsearch
import ast
import sqlite3

main = Blueprint('main', __name__)

es = Elasticsearch()

@main.route('/', methods=['GET', 'POST'])
#@login_required
def index():

    # username = current_user.username

    # user_data = User.query.filter(
    #     and_(User.username == username)
    # )

    user_defaults = []

    # for i in user_data:
    #     user_defaults.append(i.pref_location)
    #     user_defaults.append(i.pref_news_type)

    # location = user_defaults[0]

    today = datetime.now().strftime("%d %B, %Y")
    today_date = datetime.now()
    today_date = str(today_date).split(" ", 1)[0]

    con = sqlite3.connect("news/db/db.db")

    cur = con.cursor()

    title_sql_query = "SELECT x.title, COUNT(DISTINCT x.[title]) FROM (SELECT [title] FROM [au_news] UNION ALL SELECT [title] FROM [ca_news]\
    UNION ALL SELECT [title] FROM [gb_news] UNION  SELECT [title] FROM [nz_news] UNION  SELECT [title] FROM [us_news]\
    UNION  SELECT [title] FROM [za_news]) x GROUP BY x.title"
    cur.execute(title_sql_query)
    total_titles = (list(cur))
    total_titles = len(total_titles)

    author_sql_query = "SELECT x.author, COUNT(DISTINCT x.[author]) FROM (SELECT [author] FROM [au_news] UNION ALL SELECT [author] FROM [ca_news]\
    UNION ALL SELECT [author] FROM [gb_news] UNION  SELECT [author] FROM [nz_news] UNION  SELECT [author] FROM [us_news]\
    UNION  SELECT [author] FROM [za_news]) x GROUP BY x.author"

    cur.execute(author_sql_query)
    total_authors = (list(cur))
    total_authors = len(total_authors)

    sources_sql_query = "SELECT x.source, COUNT(DISTINCT x.[source]) FROM (SELECT [source] FROM [au_news] UNION ALL SELECT [source] FROM [ca_news]\
    UNION ALL SELECT [source] FROM [gb_news] UNION  SELECT [source] FROM [nz_news] UNION  SELECT [source] FROM [us_news]\
    UNION  SELECT [source] FROM [za_news]) x GROUP BY x.source"

    cur.execute(sources_sql_query)
    total_sources = (list(cur))
    total_sources =  len(total_sources)

    con.close()

    # news_type = user_defaults[1]
    # if news_type == None:
    #     news_type = user_defaults[1]
    # else:
    #     news_type = user_defaults[1].lower()

    # default_settings = []
    # if location == "United States":
    #     defaults = us_news.query.filter(
    #         and_(us_news.news_type == news_type, us_news.publishedAt.like(f'%{today_date}%'))) \
    #         .order_by(us_news.publishedAt.desc())
    #     default_settings.append(defaults)
    #     location = 'us'
    # if location == 'South Africa':
    #     defaults = za_news.query.filter(
    #         and_(za_news.news_type == news_type, za_news.publishedAt.like(f'%{today_date}%'))) \
    #         .order_by(za_news.publishedAt.desc())
    #     default_settings.append(defaults)
    #     location = 'za'
    # if location == 'Australia':
    #     defaults = au_news.query.filter(
    #         and_(au_news.news_type == news_type, au_news.publishedAt.like(f'%{today_date}%'))) \
    #         .order_by(au_news.publishedAt.desc())
    #     default_settings.append(defaults)
    #     location = 'au'
    # if location == 'Canada':
    #     defaults = ca_news.query.filter(
    #         and_(ca_news.news_type == news_type, ca_news.publishedAt.like(f'%{today_date}%'))) \
    #         .order_by(ca_news.publishedAt.desc())
    #     default_settings.append(defaults)
    #     location = 'ca'
    # if location == 'New Zealand':
    #     defaults = nz_news.query.filter(
    #         and_(nz_news.news_type == news_type, nz_news.publishedAt.like(f'%{today_date}%'))) \
    #         .order_by(nz_news.publishedAt.desc())
    #     default_settings.append(defaults)
    #     location = 'nz'
    # if location == 'Great Britain':
    #     defaults = gb_news.query.filter(
    #         and_(gb_news.news_type == news_type, gb_news.publishedAt.like(f'%{today_date}%'))) \
    #         .order_by(gb_news.publishedAt.desc())
    #     default_settings.append(defaults)
    #     location = 'gb'

    # GET STATS #
    #########################################################
    # This shit is probably too long. Needs to be refactored.
    #########################################################
    # za_headlines = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_headlines.cnf", "r")
    # za_headlines_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_headlines_authors.cnf", "r")
    # za_headlines_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_headlines_sources.cnf", "r")

    # za_business = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_business.cnf", "r")
    # za_business_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_business_authors.cnf", "r")
    # za_business_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_business_sources.cnf", "r")


    # za_technology = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_technology.cnf", "r")
    # za_technology_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_technology_authors.cnf", "r")
    # za_technology_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_technology_sources.cnf", "r")


    # za_health = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_health.cnf", "r")
    # za_health_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_health_authors.cnf", "r")
    # za_health_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_health_sources.cnf", "r")

    # za_science = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_science.cnf", "r")
    # za_science_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_science_authors.cnf", "r")
    # za_science_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_science_sources.cnf", "r")

    # za_sports = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_sports.cnf", "r")
    # za_sports_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_sports_authors.cnf", "r")
    # za_sports_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_sports_sources.cnf", "r")

    # za_entertainment = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_entertainment.cnf", "r")
    # za_entertainment_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_entertainment_authors.cnf", "r")
    # za_entertainment_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/za/za_entertainment_sources.cnf", "r")


    # contents_za_headlines = za_headlines.read()
    # contents_za_headlines_authors = za_headlines_authors.read()
    # contenets_za_headlines_sources = za_headlines_sources.read()

    # contents_za_business = za_business.read()
    # contents_za_business_authors = za_business_authors.read()
    # contenets_za_business_sources = za_business_sources.read()

    # contents_za_technology = za_technology.read()
    # contents_za_technology_authors = za_technology_authors.read()
    # contenets_za_technology_sources = za_technology_sources.read()

    # contents_za_health = za_health.read()
    # contents_za_health_authors = za_health_authors.read()
    # contenets_za_health_sources = za_health_sources.read()

    # contents_za_science = za_science.read()
    # contents_za_science_authors = za_science_authors.read()
    # contenets_za_science_sources = za_science_sources.read()

    # contents_za_sports = za_sports.read()
    # contents_za_sports_authors = za_sports_authors.read()
    # contenets_za_sports_sources = za_sports_sources.read()

    # contents_za_entertainment = za_entertainment.read()
    # contents_za_entertainment_authors = za_entertainment_authors.read()
    # contenets_za_entertainment_sources = za_entertainment_sources.read()


    # dictionary_za_headlines = ast.literal_eval(contents_za_headlines)
    # dictionary_za_headlines_authors = ast.literal_eval(contents_za_headlines_authors)
    # dictionary_za_headlines_sources = ast.literal_eval(contenets_za_headlines_sources)

    # dictionary_za_business = ast.literal_eval(contents_za_business)
    # dictionary_za_business_authors = ast.literal_eval(contents_za_business_authors)
    # dictionary_za_business_sources = ast.literal_eval(contenets_za_business_sources)

    # dictionary_za_technology = ast.literal_eval(contents_za_technology)
    # dictionary_za_technology_authors = ast.literal_eval(contents_za_technology_authors)
    # dictionary_za_technology_sources = ast.literal_eval(contenets_za_technology_sources)

    # dictionary_za_health = ast.literal_eval(contents_za_health)
    # dictionary_za_health_authors = ast.literal_eval(contents_za_health_authors)
    # dictionary_za_health_sources = ast.literal_eval(contenets_za_health_sources)

    # dictionary_za_science = ast.literal_eval(contents_za_science)
    # dictionary_za_science_authors = ast.literal_eval(contents_za_science_authors)
    # dictionary_za_science_sources = ast.literal_eval(contenets_za_science_sources)

    # dictionary_za_sports = ast.literal_eval(contents_za_sports)
    # dictionary_za_sports_authors = ast.literal_eval(contents_za_sports_authors)
    # dictionary_za_sports_sources = ast.literal_eval(contenets_za_sports_sources)

    # dictionary_za_entertainment = ast.literal_eval(contents_za_entertainment)
    # dictionary_za_entertainment_authors = ast.literal_eval(contents_za_entertainment_authors)
    # dictionary_za_entertainment_sources = ast.literal_eval(contenets_za_entertainment_sources)


    # za_headlines.close()
    # za_headlines_authors.close()
    # za_headlines_sources.close()

    # za_business.close()
    # za_business_authors.close()
    # za_business_sources.close()

    # za_technology.close()
    # za_technology_authors.close()
    # za_technology_sources.close()

    # za_health.close()
    # za_health_authors.close()
    # za_health_sources.close()

    # za_science.close()
    # za_science_authors.close()
    # za_science_sources.close()

    # za_sports.close()
    # za_sports_authors.close()
    # za_sports_sources.close()

    # za_entertainment.close()
    # za_entertainment_authors.close()
    # za_entertainment_sources.close()


    # za_headlines = es.search(index="news_data", body=dictionary_za_headlines)
    # za_headlines_authors = es.search(index="news_data", body=dictionary_za_headlines_authors)
    # za_headlines_sources = es.search(index="news_data", body=dictionary_za_headlines_sources)

    # za_business = es.search(index="news_data", body=dictionary_za_business)
    # za_business_authors = es.search(index="news_data", body=dictionary_za_business_authors)
    # za_business_sources = es.search(index="news_data", body=dictionary_za_business_sources)

    # za_techonology = es.search(index="news_data", body=dictionary_za_technology)
    # za_techonology_authors = es.search(index="news_data", body=dictionary_za_technology_authors)
    # za_techonology_sources = es.search(index="news_data", body=dictionary_za_technology_sources)

    # za_health = es.search(index="news_data", body=dictionary_za_health)
    # za_health_authors = es.search(index="news_data", body=dictionary_za_health_authors)
    # za_health_sources = es.search(index="news_data", body=dictionary_za_health_sources)

    # za_science = es.search(index="news_data", body=dictionary_za_science)
    # za_science_authors = es.search(index="news_data", body=dictionary_za_science_authors)
    # za_science_sources = es.search(index="news_data", body=dictionary_za_science_sources)

    # za_sports = es.search(index="news_data", body=dictionary_za_sports)
    # za_sports_authors = es.search(index="news_data", body=dictionary_za_sports_authors)
    # za_sports_sources = es.search(index="news_data", body=dictionary_za_sports_sources)

    # za_entertainment = es.search(index="news_data", body=dictionary_za_entertainment)
    # za_entertainment_authors = es.search(index="news_data", body=dictionary_za_entertainment_authors)
    # za_entertainment_sources = es.search(index="news_data", body=dictionary_za_entertainment_sources)


    # total_za_headlines_titles = za_headlines['hits']['total']['value']
    # total_za_headlines_authors = za_headlines_authors['aggregations']['type_count']['value']
    # total_za_headlines_sources = za_headlines_sources['aggregations']['type_count']['value']

    # total_za_business_titles = za_business['hits']['total']['value']
    # total_za_business_authors = za_business_authors['aggregations']['type_count']['value']
    # total_za_business_sources = za_business_sources['aggregations']['type_count']['value']

    # total_za_technology_titles = za_techonology['hits']['total']['value']
    # total_za_technology_authors = za_techonology_authors['aggregations']['type_count']['value']
    # total_za_technology_sources = za_techonology_sources['aggregations']['type_count']['value']

    # total_za_health_titles = za_health['hits']['total']['value']
    # total_za_health_authors = za_health_authors['aggregations']['type_count']['value']
    # total_za_health_sources = za_health_sources['aggregations']['type_count']['value']

    # total_za_science_titles = za_science['hits']['total']['value']
    # total_za_science_authors = za_science_authors['aggregations']['type_count']['value']
    # total_za_science_sources = za_science_sources['aggregations']['type_count']['value']

    # total_za_sports_titles = za_sports['hits']['total']['value']
    # total_za_sports_authors = za_sports_authors['aggregations']['type_count']['value']
    # total_za_sports_sources = za_sports_sources['aggregations']['type_count']['value']

    # total_za_entertainment_titles = za_entertainment['hits']['total']['value']
    # total_za_entertainment_authors = za_entertainment_authors['aggregations']['type_count']['value']
    # total_za_entertainment_sources = za_entertainment_sources['aggregations']['type_count']['value']




    # #UNITED STATES

    # us_headlines = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_headlines.cnf", "r")
    # us_headlines_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_headlines_authors.cnf", "r")
    # us_headlines_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_headlines_sources.cnf", "r")

    # us_business = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_business.cnf", "r")
    # us_business_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_business_authors.cnf", "r")
    # us_business_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_business_sources.cnf", "r")


    # us_technology = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_technology.cnf", "r")
    # us_technology_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_technology_authors.cnf", "r")
    # us_technology_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_technology_sources.cnf", "r")


    # us_health = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_health.cnf", "r")
    # us_health_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_health_authors.cnf", "r")
    # us_health_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_health_sources.cnf", "r")

    # us_science = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_science.cnf", "r")
    # us_science_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_science_authors.cnf", "r")
    # us_science_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_science_sources.cnf", "r")

    # us_sports = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_sports.cnf", "r")
    # us_sports_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_sports_authors.cnf", "r")
    # us_sports_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_sports_sources.cnf", "r")

    # us_entertainment = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_entertainment.cnf", "r")
    # us_entertainment_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_entertainment_authors.cnf", "r")
    # us_entertainment_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/us/us_entertainment_sources.cnf", "r")


    # contents_us_headlines = us_headlines.read()
    # contents_us_headlines_authors = us_headlines_authors.read()
    # contenets_us_headlines_sources = us_headlines_sources.read()

    # contents_us_business = us_business.read()
    # contents_us_business_authors = us_business_authors.read()
    # contenets_us_business_sources = us_business_sources.read()

    # contents_us_technology = us_technology.read()
    # contents_us_technology_authors = us_technology_authors.read()
    # contenets_us_technology_sources = us_technology_sources.read()

    # contents_us_health = us_health.read()
    # contents_us_health_authors = us_health_authors.read()
    # contenets_us_health_sources = us_health_sources.read()

    # contents_us_science = us_science.read()
    # contents_us_science_authors = us_science_authors.read()
    # contenets_us_science_sources = us_science_sources.read()

    # contents_us_sports = us_sports.read()
    # contents_us_sports_authors = us_sports_authors.read()
    # contenets_us_sports_sources = us_sports_sources.read()

    # contents_us_entertainment = us_entertainment.read()
    # contents_us_entertainment_authors = us_entertainment_authors.read()
    # contenets_us_entertainment_sources = us_entertainment_sources.read()


    # dictionary_us_headlines = ast.literal_eval(contents_us_headlines)
    # dictionary_us_headlines_authors = ast.literal_eval(contents_us_headlines_authors)
    # dictionary_us_headlines_sources = ast.literal_eval(contenets_us_headlines_sources)

    # dictionary_us_business = ast.literal_eval(contents_us_business)
    # dictionary_us_business_authors = ast.literal_eval(contents_us_business_authors)
    # dictionary_us_business_sources = ast.literal_eval(contenets_us_business_sources)

    # dictionary_us_technology = ast.literal_eval(contents_us_technology)
    # dictionary_us_technology_authors = ast.literal_eval(contents_us_technology_authors)
    # dictionary_us_technology_sources = ast.literal_eval(contenets_us_technology_sources)

    # dictionary_us_health = ast.literal_eval(contents_us_health)
    # dictionary_us_health_authors = ast.literal_eval(contents_us_health_authors)
    # dictionary_us_health_sources = ast.literal_eval(contenets_us_health_sources)

    # dictionary_us_science = ast.literal_eval(contents_us_science)
    # dictionary_us_science_authors = ast.literal_eval(contents_us_science_authors)
    # dictionary_us_science_sources = ast.literal_eval(contenets_us_science_sources)

    # dictionary_us_sports = ast.literal_eval(contents_us_sports)
    # dictionary_us_sports_authors = ast.literal_eval(contents_us_sports_authors)
    # dictionary_us_sports_sources = ast.literal_eval(contenets_us_sports_sources)

    # dictionary_us_entertainment = ast.literal_eval(contents_us_entertainment)
    # dictionary_us_entertainment_authors = ast.literal_eval(contents_us_entertainment_authors)
    # dictionary_us_entertainment_sources = ast.literal_eval(contenets_us_entertainment_sources)


    # us_headlines.close()
    # us_headlines_authors.close()
    # us_headlines_sources.close()

    # us_business.close()
    # us_business_authors.close()
    # us_business_sources.close()

    # us_technology.close()
    # us_technology_authors.close()
    # us_technology_sources.close()

    # us_health.close()
    # us_health_authors.close()
    # us_health_sources.close()

    # us_science.close()
    # us_science_authors.close()
    # us_science_sources.close()

    # us_sports.close()
    # us_sports_authors.close()
    # us_sports_sources.close()

    # us_entertainment.close()
    # us_entertainment_authors.close()
    # us_entertainment_sources.close()


    # us_headlines = es.search(index="news_data", body=dictionary_us_headlines)
    # us_headlines_authors = es.search(index="news_data", body=dictionary_us_headlines_authors)
    # us_headlines_sources = es.search(index="news_data", body=dictionary_us_headlines_sources)

    # us_business = es.search(index="news_data", body=dictionary_us_business)
    # us_business_authors = es.search(index="news_data", body=dictionary_us_business_authors)
    # us_business_sources = es.search(index="news_data", body=dictionary_us_business_sources)

    # us_techonology = es.search(index="news_data", body=dictionary_us_technology)
    # us_techonology_authors = es.search(index="news_data", body=dictionary_us_technology_authors)
    # us_techonology_sources = es.search(index="news_data", body=dictionary_us_technology_sources)

    # us_health = es.search(index="news_data", body=dictionary_us_health)
    # us_health_authors = es.search(index="news_data", body=dictionary_us_health_authors)
    # us_health_sources = es.search(index="news_data", body=dictionary_us_health_sources)

    # us_science = es.search(index="news_data", body=dictionary_us_science)
    # us_science_authors = es.search(index="news_data", body=dictionary_us_science_authors)
    # us_science_sources = es.search(index="news_data", body=dictionary_us_science_sources)

    # us_sports = es.search(index="news_data", body=dictionary_us_sports)
    # us_sports_authors = es.search(index="news_data", body=dictionary_us_sports_authors)
    # us_sports_sources = es.search(index="news_data", body=dictionary_us_sports_sources)

    # us_entertainment = es.search(index="news_data", body=dictionary_us_entertainment)
    # us_entertainment_authors = es.search(index="news_data", body=dictionary_us_entertainment_authors)
    # us_entertainment_sources = es.search(index="news_data", body=dictionary_us_entertainment_sources)


    # total_us_headlines_titles = us_headlines['hits']['total']['value']
    # total_us_headlines_authors = us_headlines_authors['aggregations']['type_count']['value']
    # total_us_headlines_sources = us_headlines_sources['aggregations']['type_count']['value']

    # total_us_business_titles = us_business['hits']['total']['value']
    # total_us_business_authors = us_business_authors['aggregations']['type_count']['value']
    # total_us_business_sources = us_business_sources['aggregations']['type_count']['value']

    # total_us_technology_titles = us_techonology['hits']['total']['value']
    # total_us_technology_authors = us_techonology_authors['aggregations']['type_count']['value']
    # total_us_technology_sources = us_techonology_sources['aggregations']['type_count']['value']

    # total_us_health_titles = us_health['hits']['total']['value']
    # total_us_health_authors = us_health_authors['aggregations']['type_count']['value']
    # total_us_health_sources = us_health_sources['aggregations']['type_count']['value']

    # total_us_science_titles = us_science['hits']['total']['value']
    # total_us_science_authors = us_science_authors['aggregations']['type_count']['value']
    # total_us_science_sources = us_science_sources['aggregations']['type_count']['value']

    # total_us_sports_titles = us_sports['hits']['total']['value']
    # total_us_sports_authors = us_sports_authors['aggregations']['type_count']['value']
    # total_us_sports_sources = us_sports_sources['aggregations']['type_count']['value']

    # total_us_entertainment_titles = us_entertainment['hits']['total']['value']
    # total_us_entertainment_authors = us_entertainment_authors['aggregations']['type_count']['value']
    # total_us_entertainment_sources = us_entertainment_sources['aggregations']['type_count']['value']

    # #NEW ZEALAND

    # nz_headlines = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_headlines.cnf", "r")
    # nz_headlines_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_headlines_authors.cnf", "r")
    # nz_headlines_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_headlines_sources.cnf", "r")

    # nz_business = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_business.cnf", "r")
    # nz_business_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_business_authors.cnf", "r")
    # nz_business_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_business_sources.cnf", "r")


    # nz_technology = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_technology.cnf", "r")
    # nz_technology_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_technology_authors.cnf", "r")
    # nz_technology_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_technology_sources.cnf", "r")


    # nz_health = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_health.cnf", "r")
    # nz_health_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_health_authors.cnf", "r")
    # nz_health_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_health_sources.cnf", "r")

    # nz_science = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_science.cnf", "r")
    # nz_science_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_science_authors.cnf", "r")
    # nz_science_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_science_sources.cnf", "r")

    # nz_sports = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_sports.cnf", "r")
    # nz_sports_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_sports_authors.cnf", "r")
    # nz_sports_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_sports_sources.cnf", "r")

    # nz_entertainment = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_entertainment.cnf", "r")
    # nz_entertainment_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_entertainment_authors.cnf", "r")
    # nz_entertainment_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/nz/nz_entertainment_sources.cnf", "r")


    # contents_nz_headlines = nz_headlines.read()
    # contents_nz_headlines_authors = nz_headlines_authors.read()
    # contenets_nz_headlines_sources = nz_headlines_sources.read()

    # contents_nz_business = nz_business.read()
    # contents_nz_business_authors = nz_business_authors.read()
    # contenets_nz_business_sources = nz_business_sources.read()

    # contents_nz_technology = nz_technology.read()
    # contents_nz_technology_authors = nz_technology_authors.read()
    # contenets_nz_technology_sources = nz_technology_sources.read()

    # contents_nz_health = nz_health.read()
    # contents_nz_health_authors = nz_health_authors.read()
    # contenets_nz_health_sources = nz_health_sources.read()

    # contents_nz_science = nz_science.read()
    # contents_nz_science_authors = nz_science_authors.read()
    # contenets_nz_science_sources = nz_science_sources.read()

    # contents_nz_sports = nz_sports.read()
    # contents_nz_sports_authors = nz_sports_authors.read()
    # contenets_nz_sports_sources = nz_sports_sources.read()

    # contents_nz_entertainment = nz_entertainment.read()
    # contents_nz_entertainment_authors = nz_entertainment_authors.read()
    # contenets_nz_entertainment_sources = nz_entertainment_sources.read()


    # dictionary_nz_headlines = ast.literal_eval(contents_nz_headlines)
    # dictionary_nz_headlines_authors = ast.literal_eval(contents_nz_headlines_authors)
    # dictionary_nz_headlines_sources = ast.literal_eval(contenets_nz_headlines_sources)

    # dictionary_nz_business = ast.literal_eval(contents_nz_business)
    # dictionary_nz_business_authors = ast.literal_eval(contents_nz_business_authors)
    # dictionary_nz_business_sources = ast.literal_eval(contenets_nz_business_sources)

    # dictionary_nz_technology = ast.literal_eval(contents_nz_technology)
    # dictionary_nz_technology_authors = ast.literal_eval(contents_nz_technology_authors)
    # dictionary_nz_technology_sources = ast.literal_eval(contenets_nz_technology_sources)

    # dictionary_nz_health = ast.literal_eval(contents_nz_health)
    # dictionary_nz_health_authors = ast.literal_eval(contents_nz_health_authors)
    # dictionary_nz_health_sources = ast.literal_eval(contenets_nz_health_sources)

    # dictionary_nz_science = ast.literal_eval(contents_nz_science)
    # dictionary_nz_science_authors = ast.literal_eval(contents_nz_science_authors)
    # dictionary_nz_science_sources = ast.literal_eval(contenets_nz_science_sources)

    # dictionary_nz_sports = ast.literal_eval(contents_nz_sports)
    # dictionary_nz_sports_authors = ast.literal_eval(contents_nz_sports_authors)
    # dictionary_nz_sports_sources = ast.literal_eval(contenets_nz_sports_sources)

    # dictionary_nz_entertainment = ast.literal_eval(contents_nz_entertainment)
    # dictionary_nz_entertainment_authors = ast.literal_eval(contents_nz_entertainment_authors)
    # dictionary_nz_entertainment_sources = ast.literal_eval(contenets_nz_entertainment_sources)


    # nz_headlines.close()
    # nz_headlines_authors.close()
    # nz_headlines_sources.close()

    # nz_business.close()
    # nz_business_authors.close()
    # nz_business_sources.close()

    # nz_technology.close()
    # nz_technology_authors.close()
    # nz_technology_sources.close()

    # nz_health.close()
    # nz_health_authors.close()
    # nz_health_sources.close()

    # nz_science.close()
    # nz_science_authors.close()
    # nz_science_sources.close()

    # nz_sports.close()
    # nz_sports_authors.close()
    # nz_sports_sources.close()

    # nz_entertainment.close()
    # nz_entertainment_authors.close()
    # nz_entertainment_sources.close()


    # nz_headlines = es.search(index="news_data", body=dictionary_nz_headlines)
    # nz_headlines_authors = es.search(index="news_data", body=dictionary_nz_headlines_authors)
    # nz_headlines_sources = es.search(index="news_data", body=dictionary_nz_headlines_sources)

    # nz_business = es.search(index="news_data", body=dictionary_nz_business)
    # nz_business_authors = es.search(index="news_data", body=dictionary_nz_business_authors)
    # nz_business_sources = es.search(index="news_data", body=dictionary_nz_business_sources)

    # nz_techonology = es.search(index="news_data", body=dictionary_nz_technology)
    # nz_techonology_authors = es.search(index="news_data", body=dictionary_nz_technology_authors)
    # nz_techonology_sources = es.search(index="news_data", body=dictionary_nz_technology_sources)

    # nz_health = es.search(index="news_data", body=dictionary_nz_health)
    # nz_health_authors = es.search(index="news_data", body=dictionary_nz_health_authors)
    # nz_health_sources = es.search(index="news_data", body=dictionary_nz_health_sources)

    # nz_science = es.search(index="news_data", body=dictionary_nz_science)
    # nz_science_authors = es.search(index="news_data", body=dictionary_nz_science_authors)
    # nz_science_sources = es.search(index="news_data", body=dictionary_nz_science_sources)

    # nz_sports = es.search(index="news_data", body=dictionary_nz_sports)
    # nz_sports_authors = es.search(index="news_data", body=dictionary_nz_sports_authors)
    # nz_sports_sources = es.search(index="news_data", body=dictionary_nz_sports_sources)

    # nz_entertainment = es.search(index="news_data", body=dictionary_nz_entertainment)
    # nz_entertainment_authors = es.search(index="news_data", body=dictionary_nz_entertainment_authors)
    # nz_entertainment_sources = es.search(index="news_data", body=dictionary_nz_entertainment_sources)


    # total_nz_headlines_titles = nz_headlines['hits']['total']['value']
    # total_nz_headlines_authors = nz_headlines_authors['aggregations']['type_count']['value']
    # total_nz_headlines_sources = nz_headlines_sources['aggregations']['type_count']['value']

    # total_nz_business_titles = nz_business['hits']['total']['value']
    # total_nz_business_authors = nz_business_authors['aggregations']['type_count']['value']
    # total_nz_business_sources = nz_business_sources['aggregations']['type_count']['value']

    # total_nz_technology_titles = nz_techonology['hits']['total']['value']
    # total_nz_technology_authors = nz_techonology_authors['aggregations']['type_count']['value']
    # total_nz_technology_sources = nz_techonology_sources['aggregations']['type_count']['value']

    # total_nz_health_titles = nz_health['hits']['total']['value']
    # total_nz_health_authors = nz_health_authors['aggregations']['type_count']['value']
    # total_nz_health_sources = nz_health_sources['aggregations']['type_count']['value']

    # total_nz_science_titles = nz_science['hits']['total']['value']
    # total_nz_science_authors = nz_science_authors['aggregations']['type_count']['value']
    # total_nz_science_sources = nz_science_sources['aggregations']['type_count']['value']

    # total_nz_sports_titles = nz_sports['hits']['total']['value']
    # total_nz_sports_authors = nz_sports_authors['aggregations']['type_count']['value']
    # total_nz_sports_sources = nz_sports_sources['aggregations']['type_count']['value']

    # total_nz_entertainment_titles = nz_entertainment['hits']['total']['value']
    # total_nz_entertainment_authors = nz_entertainment_authors['aggregations']['type_count']['value']
    # total_nz_entertainment_sources = nz_entertainment_sources['aggregations']['type_count']['value']

    # #GREAT BRITAIN

    # gb_headlines = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_headlines.cnf", "r")
    # gb_headlines_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_headlines_authors.cnf", "r")
    # gb_headlines_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_headlines_sources.cnf", "r")

    # gb_business = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_business.cnf", "r")
    # gb_business_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_business_authors.cnf", "r")
    # gb_business_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_business_sources.cnf", "r")


    # gb_technology = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_technology.cnf", "r")
    # gb_technology_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_technology_authors.cnf", "r")
    # gb_technology_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_technology_sources.cnf", "r")


    # gb_health = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_health.cnf", "r")
    # gb_health_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_health_authors.cnf", "r")
    # gb_health_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_health_sources.cnf", "r")

    # gb_science = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_science.cnf", "r")
    # gb_science_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_science_authors.cnf", "r")
    # gb_science_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_science_sources.cnf", "r")

    # gb_sports = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_sports.cnf", "r")
    # gb_sports_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_sports_authors.cnf", "r")
    # gb_sports_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_sports_sources.cnf", "r")

    # gb_entertainment = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_entertainment.cnf", "r")
    # gb_entertainment_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_entertainment_authors.cnf", "r")
    # gb_entertainment_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/gb/gb_entertainment_sources.cnf", "r")


    # contents_gb_headlines = gb_headlines.read()
    # contents_gb_headlines_authors = gb_headlines_authors.read()
    # contenets_gb_headlines_sources = gb_headlines_sources.read()

    # contents_gb_business = gb_business.read()
    # contents_gb_business_authors = gb_business_authors.read()
    # contenets_gb_business_sources = gb_business_sources.read()

    # contents_gb_technology = gb_technology.read()
    # contents_gb_technology_authors = gb_technology_authors.read()
    # contenets_gb_technology_sources = gb_technology_sources.read()

    # contents_gb_health = gb_health.read()
    # contents_gb_health_authors = gb_health_authors.read()
    # contenets_gb_health_sources = gb_health_sources.read()

    # contents_gb_science = gb_science.read()
    # contents_gb_science_authors = gb_science_authors.read()
    # contenets_gb_science_sources = gb_science_sources.read()

    # contents_gb_sports = gb_sports.read()
    # contents_gb_sports_authors = gb_sports_authors.read()
    # contenets_gb_sports_sources = gb_sports_sources.read()

    # contents_gb_entertainment = gb_entertainment.read()
    # contents_gb_entertainment_authors = gb_entertainment_authors.read()
    # contenets_gb_entertainment_sources = gb_entertainment_sources.read()


    # dictionary_gb_headlines = ast.literal_eval(contents_gb_headlines)
    # dictionary_gb_headlines_authors = ast.literal_eval(contents_gb_headlines_authors)
    # dictionary_gb_headlines_sources = ast.literal_eval(contenets_gb_headlines_sources)

    # dictionary_gb_business = ast.literal_eval(contents_gb_business)
    # dictionary_gb_business_authors = ast.literal_eval(contents_gb_business_authors)
    # dictionary_gb_business_sources = ast.literal_eval(contenets_gb_business_sources)

    # dictionary_gb_technology = ast.literal_eval(contents_gb_technology)
    # dictionary_gb_technology_authors = ast.literal_eval(contents_gb_technology_authors)
    # dictionary_gb_technology_sources = ast.literal_eval(contenets_gb_technology_sources)

    # dictionary_gb_health = ast.literal_eval(contents_gb_health)
    # dictionary_gb_health_authors = ast.literal_eval(contents_gb_health_authors)
    # dictionary_gb_health_sources = ast.literal_eval(contenets_gb_health_sources)

    # dictionary_gb_science = ast.literal_eval(contents_gb_science)
    # dictionary_gb_science_authors = ast.literal_eval(contents_gb_science_authors)
    # dictionary_gb_science_sources = ast.literal_eval(contenets_gb_science_sources)

    # dictionary_gb_sports = ast.literal_eval(contents_gb_sports)
    # dictionary_gb_sports_authors = ast.literal_eval(contents_gb_sports_authors)
    # dictionary_gb_sports_sources = ast.literal_eval(contenets_gb_sports_sources)

    # dictionary_gb_entertainment = ast.literal_eval(contents_gb_entertainment)
    # dictionary_gb_entertainment_authors = ast.literal_eval(contents_gb_entertainment_authors)
    # dictionary_gb_entertainment_sources = ast.literal_eval(contenets_gb_entertainment_sources)


    # gb_headlines.close()
    # gb_headlines_authors.close()
    # gb_headlines_sources.close()

    # gb_business.close()
    # gb_business_authors.close()
    # gb_business_sources.close()

    # gb_technology.close()
    # gb_technology_authors.close()
    # gb_technology_sources.close()

    # gb_health.close()
    # gb_health_authors.close()
    # gb_health_sources.close()

    # gb_science.close()
    # gb_science_authors.close()
    # gb_science_sources.close()

    # gb_sports.close()
    # gb_sports_authors.close()
    # gb_sports_sources.close()

    # gb_entertainment.close()
    # gb_entertainment_authors.close()
    # gb_entertainment_sources.close()


    # gb_headlines = es.search(index="news_data", body=dictionary_gb_headlines)
    # gb_headlines_authors = es.search(index="news_data", body=dictionary_gb_headlines_authors)
    # gb_headlines_sources = es.search(index="news_data", body=dictionary_gb_headlines_sources)

    # gb_business = es.search(index="news_data", body=dictionary_gb_business)
    # gb_business_authors = es.search(index="news_data", body=dictionary_gb_business_authors)
    # gb_business_sources = es.search(index="news_data", body=dictionary_gb_business_sources)

    # gb_techonology = es.search(index="news_data", body=dictionary_gb_technology)
    # gb_techonology_authors = es.search(index="news_data", body=dictionary_gb_technology_authors)
    # gb_techonology_sources = es.search(index="news_data", body=dictionary_gb_technology_sources)

    # gb_health = es.search(index="news_data", body=dictionary_gb_health)
    # gb_health_authors = es.search(index="news_data", body=dictionary_gb_health_authors)
    # gb_health_sources = es.search(index="news_data", body=dictionary_gb_health_sources)

    # gb_science = es.search(index="news_data", body=dictionary_gb_science)
    # gb_science_authors = es.search(index="news_data", body=dictionary_gb_science_authors)
    # gb_science_sources = es.search(index="news_data", body=dictionary_gb_science_sources)

    # gb_sports = es.search(index="news_data", body=dictionary_gb_sports)
    # gb_sports_authors = es.search(index="news_data", body=dictionary_gb_sports_authors)
    # gb_sports_sources = es.search(index="news_data", body=dictionary_gb_sports_sources)

    # gb_entertainment = es.search(index="news_data", body=dictionary_gb_entertainment)
    # gb_entertainment_authors = es.search(index="news_data", body=dictionary_gb_entertainment_authors)
    # gb_entertainment_sources = es.search(index="news_data", body=dictionary_gb_entertainment_sources)


    # total_gb_headlines_titles = gb_headlines['hits']['total']['value']
    # total_gb_headlines_authors = gb_headlines_authors['aggregations']['type_count']['value']
    # total_gb_headlines_sources = gb_headlines_sources['aggregations']['type_count']['value']

    # total_gb_business_titles = gb_business['hits']['total']['value']
    # total_gb_business_authors = gb_business_authors['aggregations']['type_count']['value']
    # total_gb_business_sources = gb_business_sources['aggregations']['type_count']['value']

    # total_gb_technology_titles = gb_techonology['hits']['total']['value']
    # total_gb_technology_authors = gb_techonology_authors['aggregations']['type_count']['value']
    # total_gb_technology_sources = gb_techonology_sources['aggregations']['type_count']['value']

    # total_gb_health_titles = gb_health['hits']['total']['value']
    # total_gb_health_authors = gb_health_authors['aggregations']['type_count']['value']
    # total_gb_health_sources = gb_health_sources['aggregations']['type_count']['value']

    # total_gb_science_titles = gb_science['hits']['total']['value']
    # total_gb_science_authors = gb_science_authors['aggregations']['type_count']['value']
    # total_gb_science_sources = gb_science_sources['aggregations']['type_count']['value']

    # total_gb_sports_titles = gb_sports['hits']['total']['value']
    # total_gb_sports_authors = gb_sports_authors['aggregations']['type_count']['value']
    # total_gb_sports_sources = gb_sports_sources['aggregations']['type_count']['value']

    # total_gb_entertainment_titles = gb_entertainment['hits']['total']['value']
    # total_gb_entertainment_authors = gb_entertainment_authors['aggregations']['type_count']['value']
    # total_gb_entertainment_sources = gb_entertainment_sources['aggregations']['type_count']['value']

    # #CANADA

    # ca_headlines = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_headlines.cnf", "r")
    # ca_headlines_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_headlines_authors.cnf", "r")
    # ca_headlines_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_headlines_sources.cnf", "r")

    # ca_business = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_business.cnf", "r")
    # ca_business_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_business_authors.cnf", "r")
    # ca_business_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_business_sources.cnf", "r")


    # ca_technology = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_technology.cnf", "r")
    # ca_technology_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_technology_authors.cnf", "r")
    # ca_technology_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_technology_sources.cnf", "r")


    # ca_health = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_health.cnf", "r")
    # ca_health_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_health_authors.cnf", "r")
    # ca_health_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_health_sources.cnf", "r")

    # ca_science = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_science.cnf", "r")
    # ca_science_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_science_authors.cnf", "r")
    # ca_science_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_science_sources.cnf", "r")

    # ca_sports = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_sports.cnf", "r")
    # ca_sports_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_sports_authors.cnf", "r")
    # ca_sports_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_sports_sources.cnf", "r")

    # ca_entertainment = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_entertainment.cnf", "r")
    # ca_entertainment_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_entertainment_authors.cnf", "r")
    # ca_entertainment_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/ca/ca_entertainment_sources.cnf", "r")


    # contents_ca_headlines = ca_headlines.read()
    # contents_ca_headlines_authors = ca_headlines_authors.read()
    # contenets_ca_headlines_sources = ca_headlines_sources.read()

    # contents_ca_business = ca_business.read()
    # contents_ca_business_authors = ca_business_authors.read()
    # contenets_ca_business_sources = ca_business_sources.read()

    # contents_ca_technology = ca_technology.read()
    # contents_ca_technology_authors = ca_technology_authors.read()
    # contenets_ca_technology_sources = ca_technology_sources.read()

    # contents_ca_health = ca_health.read()
    # contents_ca_health_authors = ca_health_authors.read()
    # contenets_ca_health_sources = ca_health_sources.read()

    # contents_ca_science = ca_science.read()
    # contents_ca_science_authors = ca_science_authors.read()
    # contenets_ca_science_sources = ca_science_sources.read()

    # contents_ca_sports = ca_sports.read()
    # contents_ca_sports_authors = ca_sports_authors.read()
    # contenets_ca_sports_sources = ca_sports_sources.read()

    # contents_ca_entertainment = ca_entertainment.read()
    # contents_ca_entertainment_authors = ca_entertainment_authors.read()
    # contenets_ca_entertainment_sources = ca_entertainment_sources.read()


    # dictionary_ca_headlines = ast.literal_eval(contents_ca_headlines)
    # dictionary_ca_headlines_authors = ast.literal_eval(contents_ca_headlines_authors)
    # dictionary_ca_headlines_sources = ast.literal_eval(contenets_ca_headlines_sources)

    # dictionary_ca_business = ast.literal_eval(contents_ca_business)
    # dictionary_ca_business_authors = ast.literal_eval(contents_ca_business_authors)
    # dictionary_ca_business_sources = ast.literal_eval(contenets_ca_business_sources)

    # dictionary_ca_technology = ast.literal_eval(contents_ca_technology)
    # dictionary_ca_technology_authors = ast.literal_eval(contents_ca_technology_authors)
    # dictionary_ca_technology_sources = ast.literal_eval(contenets_ca_technology_sources)

    # dictionary_ca_health = ast.literal_eval(contents_ca_health)
    # dictionary_ca_health_authors = ast.literal_eval(contents_ca_health_authors)
    # dictionary_ca_health_sources = ast.literal_eval(contenets_ca_health_sources)

    # dictionary_ca_science = ast.literal_eval(contents_ca_science)
    # dictionary_ca_science_authors = ast.literal_eval(contents_ca_science_authors)
    # dictionary_ca_science_sources = ast.literal_eval(contenets_ca_science_sources)

    # dictionary_ca_sports = ast.literal_eval(contents_ca_sports)
    # dictionary_ca_sports_authors = ast.literal_eval(contents_ca_sports_authors)
    # dictionary_ca_sports_sources = ast.literal_eval(contenets_ca_sports_sources)

    # dictionary_ca_entertainment = ast.literal_eval(contents_ca_entertainment)
    # dictionary_ca_entertainment_authors = ast.literal_eval(contents_ca_entertainment_authors)
    # dictionary_ca_entertainment_sources = ast.literal_eval(contenets_ca_entertainment_sources)


    # ca_headlines.close()
    # ca_headlines_authors.close()
    # ca_headlines_sources.close()

    # ca_business.close()
    # ca_business_authors.close()
    # ca_business_sources.close()

    # ca_technology.close()
    # ca_technology_authors.close()
    # ca_technology_sources.close()

    # ca_health.close()
    # ca_health_authors.close()
    # ca_health_sources.close()

    # ca_science.close()
    # ca_science_authors.close()
    # ca_science_sources.close()

    # ca_sports.close()
    # ca_sports_authors.close()
    # ca_sports_sources.close()

    # ca_entertainment.close()
    # ca_entertainment_authors.close()
    # ca_entertainment_sources.close()


    # ca_headlines = es.search(index="news_data", body=dictionary_ca_headlines)
    # ca_headlines_authors = es.search(index="news_data", body=dictionary_ca_headlines_authors)
    # ca_headlines_sources = es.search(index="news_data", body=dictionary_ca_headlines_sources)

    # ca_business = es.search(index="news_data", body=dictionary_ca_business)
    # ca_business_authors = es.search(index="news_data", body=dictionary_ca_business_authors)
    # ca_business_sources = es.search(index="news_data", body=dictionary_ca_business_sources)

    # ca_techonology = es.search(index="news_data", body=dictionary_ca_technology)
    # ca_techonology_authors = es.search(index="news_data", body=dictionary_ca_technology_authors)
    # ca_techonology_sources = es.search(index="news_data", body=dictionary_ca_technology_sources)

    # ca_health = es.search(index="news_data", body=dictionary_ca_health)
    # ca_health_authors = es.search(index="news_data", body=dictionary_ca_health_authors)
    # ca_health_sources = es.search(index="news_data", body=dictionary_ca_health_sources)

    # ca_science = es.search(index="news_data", body=dictionary_ca_science)
    # ca_science_authors = es.search(index="news_data", body=dictionary_ca_science_authors)
    # ca_science_sources = es.search(index="news_data", body=dictionary_ca_science_sources)

    # ca_sports = es.search(index="news_data", body=dictionary_ca_sports)
    # ca_sports_authors = es.search(index="news_data", body=dictionary_ca_sports_authors)
    # ca_sports_sources = es.search(index="news_data", body=dictionary_ca_sports_sources)

    # ca_entertainment = es.search(index="news_data", body=dictionary_ca_entertainment)
    # ca_entertainment_authors = es.search(index="news_data", body=dictionary_ca_entertainment_authors)
    # ca_entertainment_sources = es.search(index="news_data", body=dictionary_ca_entertainment_sources)


    # total_ca_headlines_titles = ca_headlines['hits']['total']['value']
    # total_ca_headlines_authors = ca_headlines_authors['aggregations']['type_count']['value']
    # total_ca_headlines_sources = ca_headlines_sources['aggregations']['type_count']['value']

    # total_ca_business_titles = ca_business['hits']['total']['value']
    # total_ca_business_authors = ca_business_authors['aggregations']['type_count']['value']
    # total_ca_business_sources = ca_business_sources['aggregations']['type_count']['value']

    # total_ca_technology_titles = ca_techonology['hits']['total']['value']
    # total_ca_technology_authors = ca_techonology_authors['aggregations']['type_count']['value']
    # total_ca_technology_sources = ca_techonology_sources['aggregations']['type_count']['value']

    # total_ca_health_titles = ca_health['hits']['total']['value']
    # total_ca_health_authors = ca_health_authors['aggregations']['type_count']['value']
    # total_ca_health_sources = ca_health_sources['aggregations']['type_count']['value']

    # total_ca_science_titles = ca_science['hits']['total']['value']
    # total_ca_science_authors = ca_science_authors['aggregations']['type_count']['value']
    # total_ca_science_sources = ca_science_sources['aggregations']['type_count']['value']

    # total_ca_sports_titles = ca_sports['hits']['total']['value']
    # total_ca_sports_authors = ca_sports_authors['aggregations']['type_count']['value']
    # total_ca_sports_sources = ca_sports_sources['aggregations']['type_count']['value']

    # total_ca_entertainment_titles = ca_entertainment['hits']['total']['value']
    # total_ca_entertainment_authors = ca_entertainment_authors['aggregations']['type_count']['value']
    # total_ca_entertainment_sources = ca_entertainment_sources['aggregations']['type_count']['value']

    # #AUSTRALIA

    # au_headlines = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_headlines.cnf", "r")
    # au_headlines_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_headlines_authors.cnf", "r")
    # au_headlines_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_headlines_sources.cnf", "r")

    # au_business = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_business.cnf", "r")
    # au_business_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_business_authors.cnf", "r")
    # au_business_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_business_sources.cnf", "r")


    # au_technology = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_technology.cnf", "r")
    # au_technology_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_technology_authors.cnf", "r")
    # au_technology_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_technology_sources.cnf", "r")


    # au_health = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_health.cnf", "r")
    # au_health_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_health_authors.cnf", "r")
    # au_health_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_health_sources.cnf", "r")

    # au_science = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_science.cnf", "r")
    # au_science_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_science_authors.cnf", "r")
    # au_science_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_science_sources.cnf", "r")

    # au_sports = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_sports.cnf", "r")
    # au_sports_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_sports_authors.cnf", "r")
    # au_sports_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_sports_sources.cnf", "r")

    # au_entertainment = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_entertainment.cnf", "r")
    # au_entertainment_authors = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_entertainment_authors.cnf", "r")
    # au_entertainment_sources = open("/Users/michael.hyland/python_prod/news_archive/news/analytics/au/au_entertainment_sources.cnf", "r")


    # contents_au_headlines = au_headlines.read()
    # contents_au_headlines_authors = au_headlines_authors.read()
    # contenets_au_headlines_sources = au_headlines_sources.read()

    # contents_au_business = au_business.read()
    # contents_au_business_authors = au_business_authors.read()
    # contenets_au_business_sources = au_business_sources.read()

    # contents_au_technology = au_technology.read()
    # contents_au_technology_authors = au_technology_authors.read()
    # contenets_au_technology_sources = au_technology_sources.read()

    # contents_au_health = au_health.read()
    # contents_au_health_authors = au_health_authors.read()
    # contenets_au_health_sources = au_health_sources.read()

    # contents_au_science = au_science.read()
    # contents_au_science_authors = au_science_authors.read()
    # contenets_au_science_sources = au_science_sources.read()

    # contents_au_sports = au_sports.read()
    # contents_au_sports_authors = au_sports_authors.read()
    # contenets_au_sports_sources = au_sports_sources.read()

    # contents_au_entertainment = au_entertainment.read()
    # contents_au_entertainment_authors = au_entertainment_authors.read()
    # contenets_au_entertainment_sources = au_entertainment_sources.read()


    # dictionary_au_headlines = ast.literal_eval(contents_au_headlines)
    # dictionary_au_headlines_authors = ast.literal_eval(contents_au_headlines_authors)
    # dictionary_au_headlines_sources = ast.literal_eval(contenets_au_headlines_sources)

    # dictionary_au_business = ast.literal_eval(contents_au_business)
    # dictionary_au_business_authors = ast.literal_eval(contents_au_business_authors)
    # dictionary_au_business_sources = ast.literal_eval(contenets_au_business_sources)

    # dictionary_au_technology = ast.literal_eval(contents_au_technology)
    # dictionary_au_technology_authors = ast.literal_eval(contents_au_technology_authors)
    # dictionary_au_technology_sources = ast.literal_eval(contenets_au_technology_sources)

    # dictionary_au_health = ast.literal_eval(contents_au_health)
    # dictionary_au_health_authors = ast.literal_eval(contents_au_health_authors)
    # dictionary_au_health_sources = ast.literal_eval(contenets_au_health_sources)

    # dictionary_au_science = ast.literal_eval(contents_au_science)
    # dictionary_au_science_authors = ast.literal_eval(contents_au_science_authors)
    # dictionary_au_science_sources = ast.literal_eval(contenets_au_science_sources)

    # dictionary_au_sports = ast.literal_eval(contents_au_sports)
    # dictionary_au_sports_authors = ast.literal_eval(contents_au_sports_authors)
    # dictionary_au_sports_sources = ast.literal_eval(contenets_au_sports_sources)

    # dictionary_au_entertainment = ast.literal_eval(contents_au_entertainment)
    # dictionary_au_entertainment_authors = ast.literal_eval(contents_au_entertainment_authors)
    # dictionary_au_entertainment_sources = ast.literal_eval(contenets_au_entertainment_sources)


    # au_headlines.close()
    # au_headlines_authors.close()
    # au_headlines_sources.close()

    # au_business.close()
    # au_business_authors.close()
    # au_business_sources.close()

    # au_technology.close()
    # au_technology_authors.close()
    # au_technology_sources.close()

    # au_health.close()
    # au_health_authors.close()
    # au_health_sources.close()

    # au_science.close()
    # au_science_authors.close()
    # au_science_sources.close()

    # au_sports.close()
    # au_sports_authors.close()
    # au_sports_sources.close()

    # au_entertainment.close()
    # au_entertainment_authors.close()
    # au_entertainment_sources.close()


    # au_headlines = es.search(index="news_data", body=dictionary_au_headlines)
    # au_headlines_authors = es.search(index="news_data", body=dictionary_au_headlines_authors)
    # au_headlines_sources = es.search(index="news_data", body=dictionary_au_headlines_sources)

    # au_business = es.search(index="news_data", body=dictionary_au_business)
    # au_business_authors = es.search(index="news_data", body=dictionary_au_business_authors)
    # au_business_sources = es.search(index="news_data", body=dictionary_au_business_sources)

    # au_techonology = es.search(index="news_data", body=dictionary_au_technology)
    # au_techonology_authors = es.search(index="news_data", body=dictionary_au_technology_authors)
    # au_techonology_sources = es.search(index="news_data", body=dictionary_au_technology_sources)

    # au_health = es.search(index="news_data", body=dictionary_au_health)
    # au_health_authors = es.search(index="news_data", body=dictionary_au_health_authors)
    # au_health_sources = es.search(index="news_data", body=dictionary_au_health_sources)

    # au_science = es.search(index="news_data", body=dictionary_au_science)
    # au_science_authors = es.search(index="news_data", body=dictionary_au_science_authors)
    # au_science_sources = es.search(index="news_data", body=dictionary_au_science_sources)

    # au_sports = es.search(index="news_data", body=dictionary_au_sports)
    # au_sports_authors = es.search(index="news_data", body=dictionary_au_sports_authors)
    # au_sports_sources = es.search(index="news_data", body=dictionary_au_sports_sources)

    # au_entertainment = es.search(index="news_data", body=dictionary_au_entertainment)
    # au_entertainment_authors = es.search(index="news_data", body=dictionary_au_entertainment_authors)
    # au_entertainment_sources = es.search(index="news_data", body=dictionary_au_entertainment_sources)


    # total_au_headlines_titles = au_headlines['hits']['total']['value']
    # total_au_headlines_authors = au_headlines_authors['aggregations']['type_count']['value']
    # total_au_headlines_sources = au_headlines_sources['aggregations']['type_count']['value']

    # total_au_business_titles = au_business['hits']['total']['value']
    # total_au_business_authors = au_business_authors['aggregations']['type_count']['value']
    # total_au_business_sources = au_business_sources['aggregations']['type_count']['value']

    # total_au_technology_titles = au_techonology['hits']['total']['value']
    # total_au_technology_authors = au_techonology_authors['aggregations']['type_count']['value']
    # total_au_technology_sources = au_techonology_sources['aggregations']['type_count']['value']

    # total_au_health_titles = au_health['hits']['total']['value']
    # total_au_health_authors = au_health_authors['aggregations']['type_count']['value']
    # total_au_health_sources = au_health_sources['aggregations']['type_count']['value']

    # total_au_science_titles = au_science['hits']['total']['value']
    # total_au_science_authors = au_science_authors['aggregations']['type_count']['value']
    # total_au_science_sources = au_science_sources['aggregations']['type_count']['value']

    # total_au_sports_titles = au_sports['hits']['total']['value']
    # total_au_sports_authors = au_sports_authors['aggregations']['type_count']['value']
    # total_au_sports_sources = au_sports_sources['aggregations']['type_count']['value']

    # total_au_entertainment_titles = au_entertainment['hits']['total']['value']
    # total_au_entertainment_authors = au_entertainment_authors['aggregations']['type_count']['value']
    # total_au_entertainment_sources = au_entertainment_sources['aggregations']['type_count']['value']


    return render_template('main/index.html', today=today, total_titles=total_titles, total_authors=total_authors, total_sources=total_sources)
                        # username=username, user_data=user_data, default_settings=default_settings, news_type=news_type,location=location
                        #      total_au_headlines_titles=total_au_headlines_titles,
                        #    total_au_headlines_authors=total_au_headlines_authors, total_au_headlines_sources=total_au_headlines_sources,
                        #    total_au_business_titles=total_au_business_titles, total_au_business_authors=total_au_business_authors,
                        #    total_au_business_sources=total_au_business_sources, total_au_technology_titles=total_au_technology_titles,
                        #    total_au_technology_authors=total_au_technology_authors, total_au_technology_sources=total_au_technology_sources,
                        #    total_au_health_titles=total_au_health_titles, total_au_health_authors=total_au_health_authors, total_au_health_sources=total_au_health_sources,
                        #    total_au_science_titles=total_au_science_titles, total_au_science_authors=total_au_science_authors, total_au_science_sources=total_au_science_sources,
                        #    total_au_sports_titles=total_au_sports_titles, total_au_sports_authors=total_au_sports_authors, total_au_sports_sources=total_au_sports_sources,
                        #    total_au_entertainment_titles=total_au_entertainment_titles, total_au_entertainment_authors=total_au_entertainment_authors,
                        #    total_au_entertainment_sources=total_au_entertainment_sources,total_ca_headlines_titles=total_ca_headlines_titles,
                        #    total_ca_headlines_authors=total_ca_headlines_authors, total_ca_headlines_sources=total_ca_headlines_sources,
                        #    total_ca_business_titles=total_ca_business_titles, total_ca_business_authors=total_ca_business_authors,
                        #    total_ca_business_sources=total_ca_business_sources, total_ca_technology_titles=total_ca_technology_titles,
                        #    total_ca_technology_authors=total_ca_technology_authors, total_ca_technology_sources=total_ca_technology_sources,
                        #    total_ca_health_titles=total_ca_health_titles, total_ca_health_authors=total_ca_health_authors, total_ca_health_sources=total_ca_health_sources,
                        #    total_ca_science_titles=total_ca_science_titles, total_ca_science_authors=total_ca_science_authors, total_ca_science_sources=total_ca_science_sources,
                        #    total_ca_sports_titles=total_ca_sports_titles, total_ca_sports_authors=total_ca_sports_authors, total_ca_sports_sources=total_ca_sports_sources,
                        #    total_ca_entertainment_titles=total_ca_entertainment_titles, total_ca_entertainment_authors=total_ca_entertainment_authors,
                        #    total_ca_entertainment_sources=total_ca_entertainment_sources,total_gb_headlines_titles=total_gb_headlines_titles,
                        #    total_gb_headlines_authors=total_gb_headlines_authors, total_gb_headlines_sources=total_gb_headlines_sources,
                        #    total_gb_business_titles=total_gb_business_titles, total_gb_business_authors=total_gb_business_authors,
                        #    total_gb_business_sources=total_gb_business_sources, total_gb_technology_titles=total_gb_technology_titles,
                        #    total_gb_technology_authors=total_gb_technology_authors, total_gb_technology_sources=total_gb_technology_sources,
                        #    total_gb_health_titles=total_gb_health_titles, total_gb_health_authors=total_gb_health_authors, total_gb_health_sources=total_gb_health_sources,
                        #    total_gb_science_titles=total_gb_science_titles, total_gb_science_authors=total_gb_science_authors, total_gb_science_sources=total_gb_science_sources,
                        #    total_gb_sports_titles=total_gb_sports_titles, total_gb_sports_authors=total_gb_sports_authors, total_gb_sports_sources=total_gb_sports_sources,
                        #    total_gb_entertainment_titles=total_gb_entertainment_titles, total_gb_entertainment_authors=total_gb_entertainment_authors,
                        #    total_gb_entertainment_sources=total_gb_entertainment_sources,total_nz_headlines_titles=total_nz_headlines_titles,
                        #    total_nz_headlines_authors=total_nz_headlines_authors, total_nz_headlines_sources=total_nz_headlines_sources,
                        #    total_nz_business_titles=total_nz_business_titles, total_nz_business_authors=total_nz_business_authors,
                        #    total_nz_business_sources=total_nz_business_sources, total_nz_technology_titles=total_nz_technology_titles,
                        #    total_nz_technology_authors=total_nz_technology_authors, total_nz_technology_sources=total_nz_technology_sources,
                        #    total_nz_health_titles=total_nz_health_titles, total_nz_health_authors=total_nz_health_authors, total_nz_health_sources=total_nz_health_sources,
                        #    total_nz_science_titles=total_nz_science_titles, total_nz_science_authors=total_nz_science_authors, total_nz_science_sources=total_nz_science_sources,
                        #    total_nz_sports_titles=total_nz_sports_titles, total_nz_sports_authors=total_nz_sports_authors, total_nz_sports_sources=total_nz_sports_sources,
                        #    total_nz_entertainment_titles=total_nz_entertainment_titles, total_nz_entertainment_authors=total_nz_entertainment_authors,
                        #    total_nz_entertainment_sources=total_nz_entertainment_sources, total_za_headlines_titles=total_za_headlines_titles,
                        #    total_za_headlines_authors=total_za_headlines_authors, total_za_headlines_sources=total_za_headlines_sources,
                        #    total_za_business_titles=total_za_business_titles, total_za_business_authors=total_za_business_authors,
                        #    total_za_business_sources=total_za_business_sources, total_za_technology_titles=total_za_technology_titles,
                        #    total_za_technology_authors=total_za_technology_authors, total_za_technology_sources=total_za_technology_sources,
                        #    total_za_health_titles=total_za_health_titles, total_za_health_authors=total_za_health_authors, total_za_health_sources=total_za_health_sources,
                        #    total_za_science_titles=total_za_science_titles, total_za_science_authors=total_za_science_authors, total_za_science_sources=total_za_science_sources,
                        #    total_za_sports_titles=total_za_sports_titles, total_za_sports_authors=total_za_sports_authors, total_za_sports_sources=total_za_sports_sources,
                        #    total_za_entertainment_titles=total_za_entertainment_titles, total_za_entertainment_authors=total_za_entertainment_authors,
                        #    total_za_entertainment_sources=total_za_entertainment_sources, total_us_headlines_titles=total_us_headlines_titles,
                        #    total_us_headlines_authors=total_us_headlines_authors, total_us_headlines_sources=total_us_headlines_sources,
                        #    total_us_business_titles=total_us_business_titles, total_us_business_authors=total_us_business_authors,
                        #    total_us_business_sources=total_us_business_sources, total_us_technology_titles=total_us_technology_titles,
                        #    total_us_technology_authors=total_us_technology_authors, total_us_technology_sources=total_us_technology_sources,
                        #    total_us_health_titles=total_us_health_titles, total_us_health_authors=total_us_health_authors, total_us_health_sources=total_us_health_sources,
                        #    total_us_science_titles=total_us_science_titles, total_us_science_authors=total_us_science_authors, total_us_science_sources=total_us_science_sources,
                        #    total_us_sports_titles=total_us_sports_titles, total_us_sports_authors=total_us_sports_authors, total_us_sports_sources=total_us_sports_sources,
                        #    total_us_entertainment_titles=total_us_entertainment_titles, total_us_entertainment_authors=total_us_entertainment_authors)

@main.route('/profile', methods=['GET', 'POST'])
#@login_required
def profile():

    today = datetime.now().strftime("%d %B, %Y")
    username = current_user.username
    user_data = User.query.filter(
    and_(User.username == username)
    )

    return render_template('main/profile.html', today=today, username=username, user_data=user_data)


@main.route('/comments', methods=['GET', 'POST'])
#@login_required
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
#@login_required
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

        return redirect(url_for('main.index'))


@main.route('/sso/', methods=['GET', 'POST'])
#@login_required
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

