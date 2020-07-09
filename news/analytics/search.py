#! /usr/bin/env python

from elasticsearch import Elasticsearch
import ast

es = Elasticsearch()

#SOUTH AFRICA

za_headlines = open("za/za_headlines.cnf", "r")
za_headlines_authors = open("za/za_headlines_authors.cnf", "r")
za_headlines_sources = open("za/za_headlines_sources.cnf", "r")

za_business = open("za/za_business.cnf", "r")
za_business_authors = open("za/za_business_authors.cnf", "r")
za_business_sources = open("za/za_business_sources.cnf", "r")


za_technology = open("za/za_technology.cnf", "r")
za_technology_authors = open("za/za_technology_authors.cnf", "r")
za_technology_sources = open("za/za_technology_sources.cnf", "r")


za_health = open("za/za_health.cnf", "r")
za_health_authors = open("za/za_health_authors.cnf", "r")
za_health_sources = open("za/za_health_sources.cnf", "r")

za_science = open("za/za_science.cnf", "r")
za_science_authors = open("za/za_science_authors.cnf", "r")
za_science_sources = open("za/za_science_sources.cnf", "r")

za_sports = open("za/za_sports.cnf", "r")
za_sports_authors = open("za/za_sports_authors.cnf", "r")
za_sports_sources = open("za/za_sports_sources.cnf", "r")

za_entertainment = open("za/za_entertainment.cnf", "r")
za_entertainment_authors = open("za/za_entertainment_authors.cnf", "r")
za_entertainment_sources = open("za/za_entertainment_sources.cnf", "r")


contents_za_headlines = za_headlines.read()
contents_za_headlines_authors = za_headlines_authors.read()
contenets_za_headlines_sources = za_headlines_sources.read()

contents_za_business = za_business.read()
contents_za_business_authors = za_business_authors.read()
contenets_za_business_sources = za_business_sources.read()

contents_za_technology = za_technology.read()
contents_za_technology_authors = za_technology_authors.read()
contenets_za_technology_sources = za_technology_sources.read()

contents_za_health = za_health.read()
contents_za_health_authors = za_health_authors.read()
contenets_za_health_sources = za_health_sources.read()

contents_za_science = za_science.read()
contents_za_science_authors = za_science_authors.read()
contenets_za_science_sources = za_science_sources.read()

contents_za_sports = za_sports.read()
contents_za_sports_authors = za_sports_authors.read()
contenets_za_sports_sources = za_sports_sources.read()

contents_za_entertainment = za_entertainment.read()
contents_za_entertainment_authors = za_entertainment_authors.read()
contenets_za_entertainment_sources = za_entertainment_sources.read()


dictionary_za_headlines = ast.literal_eval(contents_za_headlines)
dictionary_za_headlines_authors = ast.literal_eval(contents_za_headlines_authors)
dictionary_za_headlines_sources = ast.literal_eval(contenets_za_headlines_sources)

dictionary_za_business = ast.literal_eval(contents_za_business)
dictionary_za_business_authors = ast.literal_eval(contents_za_business_authors)
dictionary_za_business_sources = ast.literal_eval(contenets_za_business_sources)

dictionary_za_technology = ast.literal_eval(contents_za_technology)
dictionary_za_technology_authors = ast.literal_eval(contents_za_technology_authors)
dictionary_za_technology_sources = ast.literal_eval(contenets_za_technology_sources)

dictionary_za_health = ast.literal_eval(contents_za_health)
dictionary_za_health_authors = ast.literal_eval(contents_za_health_authors)
dictionary_za_health_sources = ast.literal_eval(contenets_za_health_sources)

dictionary_za_science = ast.literal_eval(contents_za_science)
dictionary_za_science_authors = ast.literal_eval(contents_za_science_authors)
dictionary_za_science_sources = ast.literal_eval(contenets_za_science_sources)

dictionary_za_sports = ast.literal_eval(contents_za_sports)
dictionary_za_sports_authors = ast.literal_eval(contents_za_sports_authors)
dictionary_za_sports_sources = ast.literal_eval(contenets_za_sports_sources)

dictionary_za_entertainment = ast.literal_eval(contents_za_entertainment)
dictionary_za_entertainment_authors = ast.literal_eval(contents_za_entertainment_authors)
dictionary_za_entertainment_sources = ast.literal_eval(contenets_za_entertainment_sources)


za_headlines.close()
za_headlines_authors.close()
za_headlines_sources.close()

za_business.close()
za_business_authors.close()
za_business_sources.close()

za_technology.close()
za_technology_authors.close()
za_technology_sources.close()

za_health.close()
za_health_authors.close()
za_health_sources.close()

za_science.close()
za_science_authors.close()
za_science_sources.close()

za_sports.close()
za_sports_authors.close()
za_sports_sources.close()

za_entertainment.close()
za_entertainment_authors.close()
za_entertainment_sources.close()


za_headlines = es.search(index="news_data", body=dictionary_za_headlines)
za_headlines_authors = es.search(index="news_data", body=dictionary_za_headlines_authors)
za_headlines_sources = es.search(index="news_data", body=dictionary_za_headlines_sources)

za_business = es.search(index="news_data", body=dictionary_za_business)
za_business_authors = es.search(index="news_data", body=dictionary_za_business_authors)
za_business_sources = es.search(index="news_data", body=dictionary_za_business_sources)

za_techonology = es.search(index="news_data", body=dictionary_za_technology)
za_techonology_authors = es.search(index="news_data", body=dictionary_za_technology_authors)
za_techonology_sources = es.search(index="news_data", body=dictionary_za_technology_sources)

za_health = es.search(index="news_data", body=dictionary_za_health)
za_health_authors = es.search(index="news_data", body=dictionary_za_health_authors)
za_health_sources = es.search(index="news_data", body=dictionary_za_health_sources)

za_science = es.search(index="news_data", body=dictionary_za_science)
za_science_authors = es.search(index="news_data", body=dictionary_za_science_authors)
za_science_sources = es.search(index="news_data", body=dictionary_za_science_sources)

za_sports = es.search(index="news_data", body=dictionary_za_sports)
za_sports_authors = es.search(index="news_data", body=dictionary_za_sports_authors)
za_sports_sources = es.search(index="news_data", body=dictionary_za_sports_sources)

za_entertainment = es.search(index="news_data", body=dictionary_za_entertainment)
za_entertainment_authors = es.search(index="news_data", body=dictionary_za_entertainment_authors)
za_entertainment_sources = es.search(index="news_data", body=dictionary_za_entertainment_sources)


total_za_headlines_titles = za_headlines['hits']['total']['value']
total_za_headlines_authors = za_headlines_authors['aggregations']['type_count']['value']
total_za_headlines_sources = za_headlines_sources['aggregations']['type_count']['value']

total_za_business_titles = za_business['hits']['total']['value']
total_za_business_authors = za_business_authors['aggregations']['type_count']['value']
total_za_business_sources = za_business_sources['aggregations']['type_count']['value']

total_za_technology_titles = za_techonology['hits']['total']['value']
total_za_technology_authors = za_techonology_authors['aggregations']['type_count']['value']
total_za_technology_sources = za_techonology_sources['aggregations']['type_count']['value']

total_za_health_titles = za_health['hits']['total']['value']
total_za_health_authors = za_health_authors['aggregations']['type_count']['value']
total_za_health_sources = za_health_sources['aggregations']['type_count']['value']

total_za_science_titles = za_science['hits']['total']['value']
total_za_science_authors = za_science_authors['aggregations']['type_count']['value']
total_za_science_sources = za_science_sources['aggregations']['type_count']['value']

total_za_sports_titles = za_sports['hits']['total']['value']
total_za_sports_authors = za_sports_authors['aggregations']['type_count']['value']
total_za_sports_sources = za_sports_sources['aggregations']['type_count']['value']

total_za_entertainment_titles = za_entertainment['hits']['total']['value']
total_za_entertainment_authors = za_entertainment_authors['aggregations']['type_count']['value']
total_za_entertainment_sources = za_entertainment_sources['aggregations']['type_count']['value']




#UNITED STATES

us_headlines = open("us/us_headlines.cnf", "r")
us_headlines_authors = open("us/us_headlines_authors.cnf", "r")
us_headlines_sources = open("us/us_headlines_sources.cnf", "r")

us_business = open("us/us_business.cnf", "r")
us_business_authors = open("us/us_business_authors.cnf", "r")
us_business_sources = open("us/us_business_sources.cnf", "r")


us_technology = open("us/us_technology.cnf", "r")
us_technology_authors = open("us/us_technology_authors.cnf", "r")
us_technology_sources = open("us/us_technology_sources.cnf", "r")


us_health = open("us/us_health.cnf", "r")
us_health_authors = open("us/us_health_authors.cnf", "r")
us_health_sources = open("us/us_health_sources.cnf", "r")

us_science = open("us/us_science.cnf", "r")
us_science_authors = open("us/us_science_authors.cnf", "r")
us_science_sources = open("us/us_science_sources.cnf", "r")

us_sports = open("us/us_sports.cnf", "r")
us_sports_authors = open("us/us_sports_authors.cnf", "r")
us_sports_sources = open("us/us_sports_sources.cnf", "r")

us_entertainment = open("us/us_entertainment.cnf", "r")
us_entertainment_authors = open("us/us_entertainment_authors.cnf", "r")
us_entertainment_sources = open("us/us_entertainment_sources.cnf", "r")


contents_us_headlines = us_headlines.read()
contents_us_headlines_authors = us_headlines_authors.read()
contenets_us_headlines_sources = us_headlines_sources.read()

contents_us_business = us_business.read()
contents_us_business_authors = us_business_authors.read()
contenets_us_business_sources = us_business_sources.read()

contents_us_technology = us_technology.read()
contents_us_technology_authors = us_technology_authors.read()
contenets_us_technology_sources = us_technology_sources.read()

contents_us_health = us_health.read()
contents_us_health_authors = us_health_authors.read()
contenets_us_health_sources = us_health_sources.read()

contents_us_science = us_science.read()
contents_us_science_authors = us_science_authors.read()
contenets_us_science_sources = us_science_sources.read()

contents_us_sports = us_sports.read()
contents_us_sports_authors = us_sports_authors.read()
contenets_us_sports_sources = us_sports_sources.read()

contents_us_entertainment = us_entertainment.read()
contents_us_entertainment_authors = us_entertainment_authors.read()
contenets_us_entertainment_sources = us_entertainment_sources.read()


dictionary_us_headlines = ast.literal_eval(contents_us_headlines)
dictionary_us_headlines_authors = ast.literal_eval(contents_us_headlines_authors)
dictionary_us_headlines_sources = ast.literal_eval(contenets_us_headlines_sources)

dictionary_us_business = ast.literal_eval(contents_us_business)
dictionary_us_business_authors = ast.literal_eval(contents_us_business_authors)
dictionary_us_business_sources = ast.literal_eval(contenets_us_business_sources)

dictionary_us_technology = ast.literal_eval(contents_us_technology)
dictionary_us_technology_authors = ast.literal_eval(contents_us_technology_authors)
dictionary_us_technology_sources = ast.literal_eval(contenets_us_technology_sources)

dictionary_us_health = ast.literal_eval(contents_us_health)
dictionary_us_health_authors = ast.literal_eval(contents_us_health_authors)
dictionary_us_health_sources = ast.literal_eval(contenets_us_health_sources)

dictionary_us_science = ast.literal_eval(contents_us_science)
dictionary_us_science_authors = ast.literal_eval(contents_us_science_authors)
dictionary_us_science_sources = ast.literal_eval(contenets_us_science_sources)

dictionary_us_sports = ast.literal_eval(contents_us_sports)
dictionary_us_sports_authors = ast.literal_eval(contents_us_sports_authors)
dictionary_us_sports_sources = ast.literal_eval(contenets_us_sports_sources)

dictionary_us_entertainment = ast.literal_eval(contents_us_entertainment)
dictionary_us_entertainment_authors = ast.literal_eval(contents_us_entertainment_authors)
dictionary_us_entertainment_sources = ast.literal_eval(contenets_us_entertainment_sources)


us_headlines.close()
us_headlines_authors.close()
us_headlines_sources.close()

us_business.close()
us_business_authors.close()
us_business_sources.close()

us_technology.close()
us_technology_authors.close()
us_technology_sources.close()

us_health.close()
us_health_authors.close()
us_health_sources.close()

us_science.close()
us_science_authors.close()
us_science_sources.close()

us_sports.close()
us_sports_authors.close()
us_sports_sources.close()

us_entertainment.close()
us_entertainment_authors.close()
us_entertainment_sources.close()


us_headlines = es.search(index="news_data", body=dictionary_us_headlines)
us_headlines_authors = es.search(index="news_data", body=dictionary_us_headlines_authors)
us_headlines_sources = es.search(index="news_data", body=dictionary_us_headlines_sources)

us_business = es.search(index="news_data", body=dictionary_us_business)
us_business_authors = es.search(index="news_data", body=dictionary_us_business_authors)
us_business_sources = es.search(index="news_data", body=dictionary_us_business_sources)

us_techonology = es.search(index="news_data", body=dictionary_us_technology)
us_techonology_authors = es.search(index="news_data", body=dictionary_us_technology_authors)
us_techonology_sources = es.search(index="news_data", body=dictionary_us_technology_sources)

us_health = es.search(index="news_data", body=dictionary_us_health)
us_health_authors = es.search(index="news_data", body=dictionary_us_health_authors)
us_health_sources = es.search(index="news_data", body=dictionary_us_health_sources)

us_science = es.search(index="news_data", body=dictionary_us_science)
us_science_authors = es.search(index="news_data", body=dictionary_us_science_authors)
us_science_sources = es.search(index="news_data", body=dictionary_us_science_sources)

us_sports = es.search(index="news_data", body=dictionary_us_sports)
us_sports_authors = es.search(index="news_data", body=dictionary_us_sports_authors)
us_sports_sources = es.search(index="news_data", body=dictionary_us_sports_sources)

us_entertainment = es.search(index="news_data", body=dictionary_us_entertainment)
us_entertainment_authors = es.search(index="news_data", body=dictionary_us_entertainment_authors)
us_entertainment_sources = es.search(index="news_data", body=dictionary_us_entertainment_sources)


total_us_headlines_titles = us_headlines['hits']['total']['value']
total_us_headlines_authors = us_headlines_authors['aggregations']['type_count']['value']
total_us_headlines_sources = us_headlines_sources['aggregations']['type_count']['value']

total_us_business_titles = us_business['hits']['total']['value']
total_us_business_authors = us_business_authors['aggregations']['type_count']['value']
total_us_business_sources = us_business_sources['aggregations']['type_count']['value']

total_us_technology_titles = us_techonology['hits']['total']['value']
total_us_technology_authors = us_techonology_authors['aggregations']['type_count']['value']
total_us_technology_sources = us_techonology_sources['aggregations']['type_count']['value']

total_us_health_titles = us_health['hits']['total']['value']
total_us_health_authors = us_health_authors['aggregations']['type_count']['value']
total_us_health_sources = us_health_sources['aggregations']['type_count']['value']

total_us_science_titles = us_science['hits']['total']['value']
total_us_science_authors = us_science_authors['aggregations']['type_count']['value']
total_us_science_sources = us_science_sources['aggregations']['type_count']['value']

total_us_sports_titles = us_sports['hits']['total']['value']
total_us_sports_authors = us_sports_authors['aggregations']['type_count']['value']
total_us_sports_sources = us_sports_sources['aggregations']['type_count']['value']

total_us_entertainment_titles = us_entertainment['hits']['total']['value']
total_us_entertainment_authors = us_entertainment_authors['aggregations']['type_count']['value']
total_us_entertainment_sources = us_entertainment_sources['aggregations']['type_count']['value']

#NEW ZEALAND

nz_headlines = open("nz/nz_headlines.cnf", "r")
nz_headlines_authors = open("nz/nz_headlines_authors.cnf", "r")
nz_headlines_sources = open("nz/nz_headlines_sources.cnf", "r")

nz_business = open("nz/nz_business.cnf", "r")
nz_business_authors = open("nz/nz_business_authors.cnf", "r")
nz_business_sources = open("nz/nz_business_sources.cnf", "r")


nz_technology = open("nz/nz_technology.cnf", "r")
nz_technology_authors = open("nz/nz_technology_authors.cnf", "r")
nz_technology_sources = open("nz/nz_technology_sources.cnf", "r")


nz_health = open("nz/nz_health.cnf", "r")
nz_health_authors = open("nz/nz_health_authors.cnf", "r")
nz_health_sources = open("nz/nz_health_sources.cnf", "r")

nz_science = open("nz/nz_science.cnf", "r")
nz_science_authors = open("nz/nz_science_authors.cnf", "r")
nz_science_sources = open("nz/nz_science_sources.cnf", "r")

nz_sports = open("nz/nz_sports.cnf", "r")
nz_sports_authors = open("nz/nz_sports_authors.cnf", "r")
nz_sports_sources = open("nz/nz_sports_sources.cnf", "r")

nz_entertainment = open("nz/nz_entertainment.cnf", "r")
nz_entertainment_authors = open("nz/nz_entertainment_authors.cnf", "r")
nz_entertainment_sources = open("nz/nz_entertainment_sources.cnf", "r")


contents_nz_headlines = nz_headlines.read()
contents_nz_headlines_authors = nz_headlines_authors.read()
contenets_nz_headlines_sources = nz_headlines_sources.read()

contents_nz_business = nz_business.read()
contents_nz_business_authors = nz_business_authors.read()
contenets_nz_business_sources = nz_business_sources.read()

contents_nz_technology = nz_technology.read()
contents_nz_technology_authors = nz_technology_authors.read()
contenets_nz_technology_sources = nz_technology_sources.read()

contents_nz_health = nz_health.read()
contents_nz_health_authors = nz_health_authors.read()
contenets_nz_health_sources = nz_health_sources.read()

contents_nz_science = nz_science.read()
contents_nz_science_authors = nz_science_authors.read()
contenets_nz_science_sources = nz_science_sources.read()

contents_nz_sports = nz_sports.read()
contents_nz_sports_authors = nz_sports_authors.read()
contenets_nz_sports_sources = nz_sports_sources.read()

contents_nz_entertainment = nz_entertainment.read()
contents_nz_entertainment_authors = nz_entertainment_authors.read()
contenets_nz_entertainment_sources = nz_entertainment_sources.read()


dictionary_nz_headlines = ast.literal_eval(contents_nz_headlines)
dictionary_nz_headlines_authors = ast.literal_eval(contents_nz_headlines_authors)
dictionary_nz_headlines_sources = ast.literal_eval(contenets_nz_headlines_sources)

dictionary_nz_business = ast.literal_eval(contents_nz_business)
dictionary_nz_business_authors = ast.literal_eval(contents_nz_business_authors)
dictionary_nz_business_sources = ast.literal_eval(contenets_nz_business_sources)

dictionary_nz_technology = ast.literal_eval(contents_nz_technology)
dictionary_nz_technology_authors = ast.literal_eval(contents_nz_technology_authors)
dictionary_nz_technology_sources = ast.literal_eval(contenets_nz_technology_sources)

dictionary_nz_health = ast.literal_eval(contents_nz_health)
dictionary_nz_health_authors = ast.literal_eval(contents_nz_health_authors)
dictionary_nz_health_sources = ast.literal_eval(contenets_nz_health_sources)

dictionary_nz_science = ast.literal_eval(contents_nz_science)
dictionary_nz_science_authors = ast.literal_eval(contents_nz_science_authors)
dictionary_nz_science_sources = ast.literal_eval(contenets_nz_science_sources)

dictionary_nz_sports = ast.literal_eval(contents_nz_sports)
dictionary_nz_sports_authors = ast.literal_eval(contents_nz_sports_authors)
dictionary_nz_sports_sources = ast.literal_eval(contenets_nz_sports_sources)

dictionary_nz_entertainment = ast.literal_eval(contents_nz_entertainment)
dictionary_nz_entertainment_authors = ast.literal_eval(contents_nz_entertainment_authors)
dictionary_nz_entertainment_sources = ast.literal_eval(contenets_nz_entertainment_sources)


nz_headlines.close()
nz_headlines_authors.close()
nz_headlines_sources.close()

nz_business.close()
nz_business_authors.close()
nz_business_sources.close()

nz_technology.close()
nz_technology_authors.close()
nz_technology_sources.close()

nz_health.close()
nz_health_authors.close()
nz_health_sources.close()

nz_science.close()
nz_science_authors.close()
nz_science_sources.close()

nz_sports.close()
nz_sports_authors.close()
nz_sports_sources.close()

nz_entertainment.close()
nz_entertainment_authors.close()
nz_entertainment_sources.close()


nz_headlines = es.search(index="news_data", body=dictionary_nz_headlines)
nz_headlines_authors = es.search(index="news_data", body=dictionary_nz_headlines_authors)
nz_headlines_sources = es.search(index="news_data", body=dictionary_nz_headlines_sources)

nz_business = es.search(index="news_data", body=dictionary_nz_business)
nz_business_authors = es.search(index="news_data", body=dictionary_nz_business_authors)
nz_business_sources = es.search(index="news_data", body=dictionary_nz_business_sources)

nz_techonology = es.search(index="news_data", body=dictionary_nz_technology)
nz_techonology_authors = es.search(index="news_data", body=dictionary_nz_technology_authors)
nz_techonology_sources = es.search(index="news_data", body=dictionary_nz_technology_sources)

nz_health = es.search(index="news_data", body=dictionary_nz_health)
nz_health_authors = es.search(index="news_data", body=dictionary_nz_health_authors)
nz_health_sources = es.search(index="news_data", body=dictionary_nz_health_sources)

nz_science = es.search(index="news_data", body=dictionary_nz_science)
nz_science_authors = es.search(index="news_data", body=dictionary_nz_science_authors)
nz_science_sources = es.search(index="news_data", body=dictionary_nz_science_sources)

nz_sports = es.search(index="news_data", body=dictionary_nz_sports)
nz_sports_authors = es.search(index="news_data", body=dictionary_nz_sports_authors)
nz_sports_sources = es.search(index="news_data", body=dictionary_nz_sports_sources)

nz_entertainment = es.search(index="news_data", body=dictionary_nz_entertainment)
nz_entertainment_authors = es.search(index="news_data", body=dictionary_nz_entertainment_authors)
nz_entertainment_sources = es.search(index="news_data", body=dictionary_nz_entertainment_sources)


total_nz_headlines_titles = nz_headlines['hits']['total']['value']
total_nz_headlines_authors = nz_headlines_authors['aggregations']['type_count']['value']
total_nz_headlines_sources = nz_headlines_sources['aggregations']['type_count']['value']

total_nz_business_titles = nz_business['hits']['total']['value']
total_nz_business_authors = nz_business_authors['aggregations']['type_count']['value']
total_nz_business_sources = nz_business_sources['aggregations']['type_count']['value']

total_nz_technology_titles = nz_techonology['hits']['total']['value']
total_nz_technology_authors = nz_techonology_authors['aggregations']['type_count']['value']
total_nz_technology_sources = nz_techonology_sources['aggregations']['type_count']['value']

total_nz_health_titles = nz_health['hits']['total']['value']
total_nz_health_authors = nz_health_authors['aggregations']['type_count']['value']
total_nz_health_sources = nz_health_sources['aggregations']['type_count']['value']

total_nz_science_titles = nz_science['hits']['total']['value']
total_nz_science_authors = nz_science_authors['aggregations']['type_count']['value']
total_nz_science_sources = nz_science_sources['aggregations']['type_count']['value']

total_nz_sports_titles = nz_sports['hits']['total']['value']
total_nz_sports_authors = nz_sports_authors['aggregations']['type_count']['value']
total_nz_sports_sources = nz_sports_sources['aggregations']['type_count']['value']

total_nz_entertainment_titles = nz_entertainment['hits']['total']['value']
total_nz_entertainment_authors = nz_entertainment_authors['aggregations']['type_count']['value']
total_nz_entertainment_sources = nz_entertainment_sources['aggregations']['type_count']['value']

#GREAT BRITAIN

gb_headlines = open("gb/gb_headlines.cnf", "r")
gb_headlines_authors = open("gb/gb_headlines_authors.cnf", "r")
gb_headlines_sources = open("gb/gb_headlines_sources.cnf", "r")

gb_business = open("gb/gb_business.cnf", "r")
gb_business_authors = open("gb/gb_business_authors.cnf", "r")
gb_business_sources = open("gb/gb_business_sources.cnf", "r")


gb_technology = open("gb/gb_technology.cnf", "r")
gb_technology_authors = open("gb/gb_technology_authors.cnf", "r")
gb_technology_sources = open("gb/gb_technology_sources.cnf", "r")


gb_health = open("gb/gb_health.cnf", "r")
gb_health_authors = open("gb/gb_health_authors.cnf", "r")
gb_health_sources = open("gb/gb_health_sources.cnf", "r")

gb_science = open("gb/gb_science.cnf", "r")
gb_science_authors = open("gb/gb_science_authors.cnf", "r")
gb_science_sources = open("gb/gb_science_sources.cnf", "r")

gb_sports = open("gb/gb_sports.cnf", "r")
gb_sports_authors = open("gb/gb_sports_authors.cnf", "r")
gb_sports_sources = open("gb/gb_sports_sources.cnf", "r")

gb_entertainment = open("gb/gb_entertainment.cnf", "r")
gb_entertainment_authors = open("gb/gb_entertainment_authors.cnf", "r")
gb_entertainment_sources = open("gb/gb_entertainment_sources.cnf", "r")


contents_gb_headlines = gb_headlines.read()
contents_gb_headlines_authors = gb_headlines_authors.read()
contenets_gb_headlines_sources = gb_headlines_sources.read()

contents_gb_business = gb_business.read()
contents_gb_business_authors = gb_business_authors.read()
contenets_gb_business_sources = gb_business_sources.read()

contents_gb_technology = gb_technology.read()
contents_gb_technology_authors = gb_technology_authors.read()
contenets_gb_technology_sources = gb_technology_sources.read()

contents_gb_health = gb_health.read()
contents_gb_health_authors = gb_health_authors.read()
contenets_gb_health_sources = gb_health_sources.read()

contents_gb_science = gb_science.read()
contents_gb_science_authors = gb_science_authors.read()
contenets_gb_science_sources = gb_science_sources.read()

contents_gb_sports = gb_sports.read()
contents_gb_sports_authors = gb_sports_authors.read()
contenets_gb_sports_sources = gb_sports_sources.read()

contents_gb_entertainment = gb_entertainment.read()
contents_gb_entertainment_authors = gb_entertainment_authors.read()
contenets_gb_entertainment_sources = gb_entertainment_sources.read()


dictionary_gb_headlines = ast.literal_eval(contents_gb_headlines)
dictionary_gb_headlines_authors = ast.literal_eval(contents_gb_headlines_authors)
dictionary_gb_headlines_sources = ast.literal_eval(contenets_gb_headlines_sources)

dictionary_gb_business = ast.literal_eval(contents_gb_business)
dictionary_gb_business_authors = ast.literal_eval(contents_gb_business_authors)
dictionary_gb_business_sources = ast.literal_eval(contenets_gb_business_sources)

dictionary_gb_technology = ast.literal_eval(contents_gb_technology)
dictionary_gb_technology_authors = ast.literal_eval(contents_gb_technology_authors)
dictionary_gb_technology_sources = ast.literal_eval(contenets_gb_technology_sources)

dictionary_gb_health = ast.literal_eval(contents_gb_health)
dictionary_gb_health_authors = ast.literal_eval(contents_gb_health_authors)
dictionary_gb_health_sources = ast.literal_eval(contenets_gb_health_sources)

dictionary_gb_science = ast.literal_eval(contents_gb_science)
dictionary_gb_science_authors = ast.literal_eval(contents_gb_science_authors)
dictionary_gb_science_sources = ast.literal_eval(contenets_gb_science_sources)

dictionary_gb_sports = ast.literal_eval(contents_gb_sports)
dictionary_gb_sports_authors = ast.literal_eval(contents_gb_sports_authors)
dictionary_gb_sports_sources = ast.literal_eval(contenets_gb_sports_sources)

dictionary_gb_entertainment = ast.literal_eval(contents_gb_entertainment)
dictionary_gb_entertainment_authors = ast.literal_eval(contents_gb_entertainment_authors)
dictionary_gb_entertainment_sources = ast.literal_eval(contenets_gb_entertainment_sources)


gb_headlines.close()
gb_headlines_authors.close()
gb_headlines_sources.close()

gb_business.close()
gb_business_authors.close()
gb_business_sources.close()

gb_technology.close()
gb_technology_authors.close()
gb_technology_sources.close()

gb_health.close()
gb_health_authors.close()
gb_health_sources.close()

gb_science.close()
gb_science_authors.close()
gb_science_sources.close()

gb_sports.close()
gb_sports_authors.close()
gb_sports_sources.close()

gb_entertainment.close()
gb_entertainment_authors.close()
gb_entertainment_sources.close()


gb_headlines = es.search(index="news_data", body=dictionary_gb_headlines)
gb_headlines_authors = es.search(index="news_data", body=dictionary_gb_headlines_authors)
gb_headlines_sources = es.search(index="news_data", body=dictionary_gb_headlines_sources)

gb_business = es.search(index="news_data", body=dictionary_gb_business)
gb_business_authors = es.search(index="news_data", body=dictionary_gb_business_authors)
gb_business_sources = es.search(index="news_data", body=dictionary_gb_business_sources)

gb_techonology = es.search(index="news_data", body=dictionary_gb_technology)
gb_techonology_authors = es.search(index="news_data", body=dictionary_gb_technology_authors)
gb_techonology_sources = es.search(index="news_data", body=dictionary_gb_technology_sources)

gb_health = es.search(index="news_data", body=dictionary_gb_health)
gb_health_authors = es.search(index="news_data", body=dictionary_gb_health_authors)
gb_health_sources = es.search(index="news_data", body=dictionary_gb_health_sources)

gb_science = es.search(index="news_data", body=dictionary_gb_science)
gb_science_authors = es.search(index="news_data", body=dictionary_gb_science_authors)
gb_science_sources = es.search(index="news_data", body=dictionary_gb_science_sources)

gb_sports = es.search(index="news_data", body=dictionary_gb_sports)
gb_sports_authors = es.search(index="news_data", body=dictionary_gb_sports_authors)
gb_sports_sources = es.search(index="news_data", body=dictionary_gb_sports_sources)

gb_entertainment = es.search(index="news_data", body=dictionary_gb_entertainment)
gb_entertainment_authors = es.search(index="news_data", body=dictionary_gb_entertainment_authors)
gb_entertainment_sources = es.search(index="news_data", body=dictionary_gb_entertainment_sources)


total_gb_headlines_titles = gb_headlines['hits']['total']['value']
total_gb_headlines_authors = gb_headlines_authors['aggregations']['type_count']['value']
total_gb_headlines_sources = gb_headlines_sources['aggregations']['type_count']['value']

total_gb_business_titles = gb_business['hits']['total']['value']
total_gb_business_authors = gb_business_authors['aggregations']['type_count']['value']
total_gb_business_sources = gb_business_sources['aggregations']['type_count']['value']

total_gb_technology_titles = gb_techonology['hits']['total']['value']
total_gb_technology_authors = gb_techonology_authors['aggregations']['type_count']['value']
total_gb_technology_sources = gb_techonology_sources['aggregations']['type_count']['value']

total_gb_health_titles = gb_health['hits']['total']['value']
total_gb_health_authors = gb_health_authors['aggregations']['type_count']['value']
total_gb_health_sources = gb_health_sources['aggregations']['type_count']['value']

total_gb_science_titles = gb_science['hits']['total']['value']
total_gb_science_authors = gb_science_authors['aggregations']['type_count']['value']
total_gb_science_sources = gb_science_sources['aggregations']['type_count']['value']

total_gb_sports_titles = gb_sports['hits']['total']['value']
total_gb_sports_authors = gb_sports_authors['aggregations']['type_count']['value']
total_gb_sports_sources = gb_sports_sources['aggregations']['type_count']['value']

total_gb_entertainment_titles = gb_entertainment['hits']['total']['value']
total_gb_entertainment_authors = gb_entertainment_authors['aggregations']['type_count']['value']
total_gb_entertainment_sources = gb_entertainment_sources['aggregations']['type_count']['value']

#CANADA

ca_headlines = open("ca/ca_headlines.cnf", "r")
ca_headlines_authors = open("ca/ca_headlines_authors.cnf", "r")
ca_headlines_sources = open("ca/ca_headlines_sources.cnf", "r")

ca_business = open("ca/ca_business.cnf", "r")
ca_business_authors = open("ca/ca_business_authors.cnf", "r")
ca_business_sources = open("ca/ca_business_sources.cnf", "r")


ca_technology = open("ca/ca_technology.cnf", "r")
ca_technology_authors = open("ca/ca_technology_authors.cnf", "r")
ca_technology_sources = open("ca/ca_technology_sources.cnf", "r")


ca_health = open("ca/ca_health.cnf", "r")
ca_health_authors = open("ca/ca_health_authors.cnf", "r")
ca_health_sources = open("ca/ca_health_sources.cnf", "r")

ca_science = open("ca/ca_science.cnf", "r")
ca_science_authors = open("ca/ca_science_authors.cnf", "r")
ca_science_sources = open("ca/ca_science_sources.cnf", "r")

ca_sports = open("ca/ca_sports.cnf", "r")
ca_sports_authors = open("ca/ca_sports_authors.cnf", "r")
ca_sports_sources = open("ca/ca_sports_sources.cnf", "r")

ca_entertainment = open("ca/ca_entertainment.cnf", "r")
ca_entertainment_authors = open("ca/ca_entertainment_authors.cnf", "r")
ca_entertainment_sources = open("ca/ca_entertainment_sources.cnf", "r")


contents_ca_headlines = ca_headlines.read()
contents_ca_headlines_authors = ca_headlines_authors.read()
contenets_ca_headlines_sources = ca_headlines_sources.read()

contents_ca_business = ca_business.read()
contents_ca_business_authors = ca_business_authors.read()
contenets_ca_business_sources = ca_business_sources.read()

contents_ca_technology = ca_technology.read()
contents_ca_technology_authors = ca_technology_authors.read()
contenets_ca_technology_sources = ca_technology_sources.read()

contents_ca_health = ca_health.read()
contents_ca_health_authors = ca_health_authors.read()
contenets_ca_health_sources = ca_health_sources.read()

contents_ca_science = ca_science.read()
contents_ca_science_authors = ca_science_authors.read()
contenets_ca_science_sources = ca_science_sources.read()

contents_ca_sports = ca_sports.read()
contents_ca_sports_authors = ca_sports_authors.read()
contenets_ca_sports_sources = ca_sports_sources.read()

contents_ca_entertainment = ca_entertainment.read()
contents_ca_entertainment_authors = ca_entertainment_authors.read()
contenets_ca_entertainment_sources = ca_entertainment_sources.read()


dictionary_ca_headlines = ast.literal_eval(contents_ca_headlines)
dictionary_ca_headlines_authors = ast.literal_eval(contents_ca_headlines_authors)
dictionary_ca_headlines_sources = ast.literal_eval(contenets_ca_headlines_sources)

dictionary_ca_business = ast.literal_eval(contents_ca_business)
dictionary_ca_business_authors = ast.literal_eval(contents_ca_business_authors)
dictionary_ca_business_sources = ast.literal_eval(contenets_ca_business_sources)

dictionary_ca_technology = ast.literal_eval(contents_ca_technology)
dictionary_ca_technology_authors = ast.literal_eval(contents_ca_technology_authors)
dictionary_ca_technology_sources = ast.literal_eval(contenets_ca_technology_sources)

dictionary_ca_health = ast.literal_eval(contents_ca_health)
dictionary_ca_health_authors = ast.literal_eval(contents_ca_health_authors)
dictionary_ca_health_sources = ast.literal_eval(contenets_ca_health_sources)

dictionary_ca_science = ast.literal_eval(contents_ca_science)
dictionary_ca_science_authors = ast.literal_eval(contents_ca_science_authors)
dictionary_ca_science_sources = ast.literal_eval(contenets_ca_science_sources)

dictionary_ca_sports = ast.literal_eval(contents_ca_sports)
dictionary_ca_sports_authors = ast.literal_eval(contents_ca_sports_authors)
dictionary_ca_sports_sources = ast.literal_eval(contenets_ca_sports_sources)

dictionary_ca_entertainment = ast.literal_eval(contents_ca_entertainment)
dictionary_ca_entertainment_authors = ast.literal_eval(contents_ca_entertainment_authors)
dictionary_ca_entertainment_sources = ast.literal_eval(contenets_ca_entertainment_sources)


ca_headlines.close()
ca_headlines_authors.close()
ca_headlines_sources.close()

ca_business.close()
ca_business_authors.close()
ca_business_sources.close()

ca_technology.close()
ca_technology_authors.close()
ca_technology_sources.close()

ca_health.close()
ca_health_authors.close()
ca_health_sources.close()

ca_science.close()
ca_science_authors.close()
ca_science_sources.close()

ca_sports.close()
ca_sports_authors.close()
ca_sports_sources.close()

ca_entertainment.close()
ca_entertainment_authors.close()
ca_entertainment_sources.close()


ca_headlines = es.search(index="news_data", body=dictionary_ca_headlines)
ca_headlines_authors = es.search(index="news_data", body=dictionary_ca_headlines_authors)
ca_headlines_sources = es.search(index="news_data", body=dictionary_ca_headlines_sources)

ca_business = es.search(index="news_data", body=dictionary_ca_business)
ca_business_authors = es.search(index="news_data", body=dictionary_ca_business_authors)
ca_business_sources = es.search(index="news_data", body=dictionary_ca_business_sources)

ca_techonology = es.search(index="news_data", body=dictionary_ca_technology)
ca_techonology_authors = es.search(index="news_data", body=dictionary_ca_technology_authors)
ca_techonology_sources = es.search(index="news_data", body=dictionary_ca_technology_sources)

ca_health = es.search(index="news_data", body=dictionary_ca_health)
ca_health_authors = es.search(index="news_data", body=dictionary_ca_health_authors)
ca_health_sources = es.search(index="news_data", body=dictionary_ca_health_sources)

ca_science = es.search(index="news_data", body=dictionary_ca_science)
ca_science_authors = es.search(index="news_data", body=dictionary_ca_science_authors)
ca_science_sources = es.search(index="news_data", body=dictionary_ca_science_sources)

ca_sports = es.search(index="news_data", body=dictionary_ca_sports)
ca_sports_authors = es.search(index="news_data", body=dictionary_ca_sports_authors)
ca_sports_sources = es.search(index="news_data", body=dictionary_ca_sports_sources)

ca_entertainment = es.search(index="news_data", body=dictionary_ca_entertainment)
ca_entertainment_authors = es.search(index="news_data", body=dictionary_ca_entertainment_authors)
ca_entertainment_sources = es.search(index="news_data", body=dictionary_ca_entertainment_sources)


total_ca_headlines_titles = ca_headlines['hits']['total']['value']
total_ca_headlines_authors = ca_headlines_authors['aggregations']['type_count']['value']
total_ca_headlines_sources = ca_headlines_sources['aggregations']['type_count']['value']

total_ca_business_titles = ca_business['hits']['total']['value']
total_ca_business_authors = ca_business_authors['aggregations']['type_count']['value']
total_ca_business_sources = ca_business_sources['aggregations']['type_count']['value']

total_ca_technology_titles = ca_techonology['hits']['total']['value']
total_ca_technology_authors = ca_techonology_authors['aggregations']['type_count']['value']
total_ca_technology_sources = ca_techonology_sources['aggregations']['type_count']['value']

total_ca_health_titles = ca_health['hits']['total']['value']
total_ca_health_authors = ca_health_authors['aggregations']['type_count']['value']
total_ca_health_sources = ca_health_sources['aggregations']['type_count']['value']

total_ca_science_titles = ca_science['hits']['total']['value']
total_ca_science_authors = ca_science_authors['aggregations']['type_count']['value']
total_ca_science_sources = ca_science_sources['aggregations']['type_count']['value']

total_ca_sports_titles = ca_sports['hits']['total']['value']
total_ca_sports_authors = ca_sports_authors['aggregations']['type_count']['value']
total_ca_sports_sources = ca_sports_sources['aggregations']['type_count']['value']

total_ca_entertainment_titles = ca_entertainment['hits']['total']['value']
total_ca_entertainment_authors = ca_entertainment_authors['aggregations']['type_count']['value']
total_ca_entertainment_sources = ca_entertainment_sources['aggregations']['type_count']['value']

#AUSTRALIA

au_headlines = open("au/au_headlines.cnf", "r")
au_headlines_authors = open("au/au_headlines_authors.cnf", "r")
au_headlines_sources = open("au/au_headlines_sources.cnf", "r")

au_business = open("au/au_business.cnf", "r")
au_business_authors = open("au/au_business_authors.cnf", "r")
au_business_sources = open("au/au_business_sources.cnf", "r")


au_technology = open("au/au_technology.cnf", "r")
au_technology_authors = open("au/au_technology_authors.cnf", "r")
au_technology_sources = open("au/au_technology_sources.cnf", "r")


au_health = open("au/au_health.cnf", "r")
au_health_authors = open("au/au_health_authors.cnf", "r")
au_health_sources = open("au/au_health_sources.cnf", "r")

au_science = open("au/au_science.cnf", "r")
au_science_authors = open("au/au_science_authors.cnf", "r")
au_science_sources = open("au/au_science_sources.cnf", "r")

au_sports = open("au/au_sports.cnf", "r")
au_sports_authors = open("au/au_sports_authors.cnf", "r")
au_sports_sources = open("au/au_sports_sources.cnf", "r")

au_entertainment = open("au/au_entertainment.cnf", "r")
au_entertainment_authors = open("au/au_entertainment_authors.cnf", "r")
au_entertainment_sources = open("au/au_entertainment_sources.cnf", "r")


contents_au_headlines = au_headlines.read()
contents_au_headlines_authors = au_headlines_authors.read()
contenets_au_headlines_sources = au_headlines_sources.read()

contents_au_business = au_business.read()
contents_au_business_authors = au_business_authors.read()
contenets_au_business_sources = au_business_sources.read()

contents_au_technology = au_technology.read()
contents_au_technology_authors = au_technology_authors.read()
contenets_au_technology_sources = au_technology_sources.read()

contents_au_health = au_health.read()
contents_au_health_authors = au_health_authors.read()
contenets_au_health_sources = au_health_sources.read()

contents_au_science = au_science.read()
contents_au_science_authors = au_science_authors.read()
contenets_au_science_sources = au_science_sources.read()

contents_au_sports = au_sports.read()
contents_au_sports_authors = au_sports_authors.read()
contenets_au_sports_sources = au_sports_sources.read()

contents_au_entertainment = au_entertainment.read()
contents_au_entertainment_authors = au_entertainment_authors.read()
contenets_au_entertainment_sources = au_entertainment_sources.read()


dictionary_au_headlines = ast.literal_eval(contents_au_headlines)
dictionary_au_headlines_authors = ast.literal_eval(contents_au_headlines_authors)
dictionary_au_headlines_sources = ast.literal_eval(contenets_au_headlines_sources)

dictionary_au_business = ast.literal_eval(contents_au_business)
dictionary_au_business_authors = ast.literal_eval(contents_au_business_authors)
dictionary_au_business_sources = ast.literal_eval(contenets_au_business_sources)

dictionary_au_technology = ast.literal_eval(contents_au_technology)
dictionary_au_technology_authors = ast.literal_eval(contents_au_technology_authors)
dictionary_au_technology_sources = ast.literal_eval(contenets_au_technology_sources)

dictionary_au_health = ast.literal_eval(contents_au_health)
dictionary_au_health_authors = ast.literal_eval(contents_au_health_authors)
dictionary_au_health_sources = ast.literal_eval(contenets_au_health_sources)

dictionary_au_science = ast.literal_eval(contents_au_science)
dictionary_au_science_authors = ast.literal_eval(contents_au_science_authors)
dictionary_au_science_sources = ast.literal_eval(contenets_au_science_sources)

dictionary_au_sports = ast.literal_eval(contents_au_sports)
dictionary_au_sports_authors = ast.literal_eval(contents_au_sports_authors)
dictionary_au_sports_sources = ast.literal_eval(contenets_au_sports_sources)

dictionary_au_entertainment = ast.literal_eval(contents_au_entertainment)
dictionary_au_entertainment_authors = ast.literal_eval(contents_au_entertainment_authors)
dictionary_au_entertainment_sources = ast.literal_eval(contenets_au_entertainment_sources)


au_headlines.close()
au_headlines_authors.close()
au_headlines_sources.close()

au_business.close()
au_business_authors.close()
au_business_sources.close()

au_technology.close()
au_technology_authors.close()
au_technology_sources.close()

au_health.close()
au_health_authors.close()
au_health_sources.close()

au_science.close()
au_science_authors.close()
au_science_sources.close()

au_sports.close()
au_sports_authors.close()
au_sports_sources.close()

au_entertainment.close()
au_entertainment_authors.close()
au_entertainment_sources.close()


au_headlines = es.search(index="news_data", body=dictionary_au_headlines)
au_headlines_authors = es.search(index="news_data", body=dictionary_au_headlines_authors)
au_headlines_sources = es.search(index="news_data", body=dictionary_au_headlines_sources)

au_business = es.search(index="news_data", body=dictionary_au_business)
au_business_authors = es.search(index="news_data", body=dictionary_au_business_authors)
au_business_sources = es.search(index="news_data", body=dictionary_au_business_sources)

au_techonology = es.search(index="news_data", body=dictionary_au_technology)
au_techonology_authors = es.search(index="news_data", body=dictionary_au_technology_authors)
au_techonology_sources = es.search(index="news_data", body=dictionary_au_technology_sources)

au_health = es.search(index="news_data", body=dictionary_au_health)
au_health_authors = es.search(index="news_data", body=dictionary_au_health_authors)
au_health_sources = es.search(index="news_data", body=dictionary_au_health_sources)

au_science = es.search(index="news_data", body=dictionary_au_science)
au_science_authors = es.search(index="news_data", body=dictionary_au_science_authors)
au_science_sources = es.search(index="news_data", body=dictionary_au_science_sources)

au_sports = es.search(index="news_data", body=dictionary_au_sports)
au_sports_authors = es.search(index="news_data", body=dictionary_au_sports_authors)
au_sports_sources = es.search(index="news_data", body=dictionary_au_sports_sources)

au_entertainment = es.search(index="news_data", body=dictionary_au_entertainment)
au_entertainment_authors = es.search(index="news_data", body=dictionary_au_entertainment_authors)
au_entertainment_sources = es.search(index="news_data", body=dictionary_au_entertainment_sources)


total_au_headlines_titles = au_headlines['hits']['total']['value']
total_au_headlines_authors = au_headlines_authors['aggregations']['type_count']['value']
total_au_headlines_sources = au_headlines_sources['aggregations']['type_count']['value']

total_au_business_titles = au_business['hits']['total']['value']
total_au_business_authors = au_business_authors['aggregations']['type_count']['value']
total_au_business_sources = au_business_sources['aggregations']['type_count']['value']

total_au_technology_titles = au_techonology['hits']['total']['value']
total_au_technology_authors = au_techonology_authors['aggregations']['type_count']['value']
total_au_technology_sources = au_techonology_sources['aggregations']['type_count']['value']

total_au_health_titles = au_health['hits']['total']['value']
total_au_health_authors = au_health_authors['aggregations']['type_count']['value']
total_au_health_sources = au_health_sources['aggregations']['type_count']['value']

total_au_science_titles = au_science['hits']['total']['value']
total_au_science_authors = au_science_authors['aggregations']['type_count']['value']
total_au_science_sources = au_science_sources['aggregations']['type_count']['value']

total_au_sports_titles = au_sports['hits']['total']['value']
total_au_sports_authors = au_sports_authors['aggregations']['type_count']['value']
total_au_sports_sources = au_sports_sources['aggregations']['type_count']['value']

total_au_entertainment_titles = au_entertainment['hits']['total']['value']
total_au_entertainment_authors = au_entertainment_authors['aggregations']['type_count']['value']
total_au_entertainment_sources = au_entertainment_sources['aggregations']['type_count']['value']

#PRINT OUT STATS
print("ZA Stats")
print("ZA Headlines Titles: " + str(total_za_headlines_titles))
print("ZA Headlines Authors: " + str(total_za_headlines_authors))
print("ZA Headlines Sources: " + str(total_za_headlines_sources))
print("\n")
print("ZA Business Titles: " + str(total_za_business_titles))
print("ZA Business Authors: " + str(total_za_business_authors))
print("ZA Business Sources: " + str(total_za_business_sources))
print("\n")
print("ZA Technology Titles: " + str(total_za_technology_titles))
print("ZA Technology Authors: " + str(total_za_technology_authors))
print("ZA Technology Sources: " + str(total_za_technology_sources))
print("\n")
print("ZA Health Titles: " + str(total_za_health_titles))
print("ZA Health Authors: " + str(total_za_health_authors))
print("ZA Health Sources: " + str(total_za_health_sources))
print("\n")
print("ZA Science Titles: " + str(total_za_science_titles))
print("ZA Science Authors: " + str(total_za_science_authors))
print("ZA Science Sources: " + str(total_za_science_sources))
print("\n")
print("ZA Sports Titles: " + str(total_za_sports_titles))
print("ZA Sports Authors: " + str(total_za_sports_authors))
print("ZA Sports Sources: " + str(total_za_sports_sources))
print("\n")
print("ZA Entertainment Titles: " + str(total_za_entertainment_titles))
print("ZA Entertainment Authors: " + str(total_za_entertainment_authors))
print("ZA Entertainment Sources: " + str(total_za_entertainment_sources))
print("***********************")
print("\n")

print("US Stats")
print("US Headlines Titles: " + str(total_us_headlines_titles))
print("US Headlines Authors: " + str(total_us_headlines_authors))
print("US Headlines Sources: " + str(total_us_headlines_sources))
print("\n")
print("US Business Titles: " + str(total_us_business_titles))
print("US Business Authors: " + str(total_us_business_authors))
print("US Business Sources: " + str(total_us_business_sources))
print("\n")
print("US Technology Titles: " + str(total_us_technology_titles))
print("US Technology Authors: " + str(total_us_technology_authors))
print("US Technology Sources: " + str(total_us_technology_sources))
print("\n")
print("US Health Titles: " + str(total_us_health_titles))
print("US Health Authors: " + str(total_us_health_authors))
print("US Health Sources: " + str(total_us_health_sources))
print("\n")
print("US Science Titles: " + str(total_us_science_titles))
print("US Science Authors: " + str(total_us_science_authors))
print("US Science Sources: " + str(total_us_science_sources))
print("\n")
print("US Sports Titles: " + str(total_us_sports_titles))
print("US Sports Authors: " + str(total_us_sports_authors))
print("US Sports Sources: " + str(total_us_sports_sources))
print("\n")
print("US Entertainment Titles: " + str(total_us_entertainment_titles))
print("US Entertainment Authors: " + str(total_us_entertainment_authors))
print("US Entertainment Sources: " + str(total_us_entertainment_sources))
print("***********************")
print("\n")

print("NZ Stats")
print("NZ Headlines Titles: " + str(total_nz_headlines_titles))
print("NZ Headlines Authors: " + str(total_nz_headlines_authors))
print("NZ Headlines Sources: " + str(total_nz_headlines_sources))
print("\n")
print("NZ business Titles: " + str(total_nz_business_titles))
print("NZ business Authors: " + str(total_nz_business_authors))
print("NZ business Sources: " + str(total_nz_business_sources))
print("\n")
print("NZ Technology Titles: " + str(total_nz_technology_titles))
print("NZ Technology Authors: " + str(total_nz_technology_authors))
print("NZ Technology Sources: " + str(total_nz_technology_sources))
print("\n")
print("NZ Health Titles: " + str(total_nz_health_titles))
print("NZ Health Authors: " + str(total_nz_health_authors))
print("NZ Health Sources: " + str(total_nz_health_sources))
print("\n")
print("NZ Science Titles: " + str(total_nz_science_titles))
print("NZ Science Authors: " + str(total_nz_science_authors))
print("NZ Science Sources: " + str(total_nz_science_sources))
print("\n")
print("NZ Sports Titles: " + str(total_nz_sports_titles))
print("NZ Sports Authors: " + str(total_nz_sports_authors))
print("NZ Sports Sources: " + str(total_nz_sports_sources))
print("\n")
print("NZ Entertainment Titles: " + str(total_nz_entertainment_titles))
print("NZ Entertainment Authors: " + str(total_nz_entertainment_authors))
print("NZ Entertainment Sources: " + str(total_nz_entertainment_sources))
print("***********************")
print("\n")

print("GB Stats")
print("GB Headlines Titles: " + str(total_gb_headlines_titles))
print("GB Headlines Authors: " + str(total_gb_headlines_authors))
print("GB Headlines Sources: " + str(total_gb_headlines_sources))
print("\n")
print("GB business Titles: " + str(total_gb_business_titles))
print("GB business Authors: " + str(total_gb_business_authors))
print("GB business Sources: " + str(total_gb_business_sources))
print("\n")
print("GB Technology Titles: " + str(total_gb_technology_titles))
print("GB Technology Authors: " + str(total_gb_technology_authors))
print("GB Technology Sources: " + str(total_gb_technology_sources))
print("\n")
print("GB Health Titles: " + str(total_gb_health_titles))
print("GB Health Authors: " + str(total_gb_health_authors))
print("GB Health Sources: " + str(total_gb_health_sources))
print("\n")
print("GB Science Titles: " + str(total_gb_science_titles))
print("GB Science Authors: " + str(total_gb_science_authors))
print("GB Science Sources: " + str(total_gb_science_sources))
print("\n")
print("GB Sports Titles: " + str(total_gb_sports_titles))
print("GB Sports Authors: " + str(total_gb_sports_authors))
print("GB Sports Sources: " + str(total_gb_sports_sources))
print("\n")
print("GB Entertainment Titles: " + str(total_gb_entertainment_titles))
print("GB Entertainment Authors: " + str(total_gb_entertainment_authors))
print("GB Entertainment Sources: " + str(total_gb_entertainment_sources))
print("***********************")
print("\n")

print("CA Stats")
print("CA Headlines Titles: " + str(total_ca_headlines_titles))
print("CA Headlines Authors: " + str(total_ca_headlines_authors))
print("CA Headlines Sources: " + str(total_ca_headlines_sources))
print("\n")
print("CA business Titles: " + str(total_ca_business_titles))
print("CA business Authors: " + str(total_ca_business_authors))
print("CA business Sources: " + str(total_ca_business_sources))
print("\n")
print("CA Technology Titles: " + str(total_ca_technology_titles))
print("CA Technology Authors: " + str(total_ca_technology_authors))
print("CA Technology Sources: " + str(total_ca_technology_sources))
print("\n")
print("CA Health Titles: " + str(total_ca_health_titles))
print("CA Health Authors: " + str(total_ca_health_authors))
print("CA Health Sources: " + str(total_ca_health_sources))
print("\n")
print("CA Science Titles: " + str(total_ca_science_titles))
print("CA Science Authors: " + str(total_ca_science_authors))
print("CA Science Sources: " + str(total_ca_science_sources))
print("\n")
print("CA Sports Titles: " + str(total_ca_sports_titles))
print("CA Sports Authors: " + str(total_ca_sports_authors))
print("CA Sports Sources: " + str(total_ca_sports_sources))
print("\n")
print("CA Entertainment Titles: " + str(total_ca_entertainment_titles))
print("CA Entertainment Authors: " + str(total_ca_entertainment_authors))
print("CA Entertainment Sources: " + str(total_ca_entertainment_sources))
print("***********************")
print("\n")

print("AU Stats")
print("AU Headlines Titles: " + str(total_au_headlines_titles))
print("AU Headlines Authors: " + str(total_au_headlines_authors))
print("AU Headlines Sources: " + str(total_au_headlines_sources))
print("\n")
print("AU business Titles: " + str(total_au_business_titles))
print("AU business Authors: " + str(total_au_business_authors))
print("AU business Sources: " + str(total_au_business_sources))
print("\n")
print("AU Technology Titles: " + str(total_au_technology_titles))
print("AU Technology Authors: " + str(total_au_technology_authors))
print("AU Technology Sources: " + str(total_au_technology_sources))
print("\n")
print("AU Health Titles: " + str(total_au_health_titles))
print("AU Health Authors: " + str(total_au_health_authors))
print("AU Health Sources: " + str(total_au_health_sources))
print("\n")
print("AU Science Titles: " + str(total_au_science_titles))
print("AU Science Authors: " + str(total_au_science_authors))
print("AU Science Sources: " + str(total_au_science_sources))
print("\n")
print("AU Sports Titles: " + str(total_au_sports_titles))
print("AU Sports Authors: " + str(total_au_sports_authors))
print("AU Sports Sources: " + str(total_au_sports_sources))
print("\n")
print("AU Entertainment Titles: " + str(total_au_entertainment_titles))
print("AU Entertainment Authors: " + str(total_au_entertainment_authors))
print("AU Entertainment Sources: " + str(total_au_entertainment_sources))
print("***********************")
print("\n")
    
    