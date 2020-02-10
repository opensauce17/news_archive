# THE WORLD NEWS ARCHIVE

The World News Archive is part of a portfolio suite featured on <a href="https://mikehyland.com" target="_blank">mikehyland.com</a>


This app utilises the <a href="https://newsapi.org/" target="_blank">News API</a> to gather and then display news articles published by world wide news outlets.

The gather.py script connects to the News API and gathers news data for selected countries and puts it into a sql lite database. 

The web application displays the news per selected country, category and date. The navigation items will display today's news in the selected categories for the selected country.

There are two search mechanisms: country specific search and advanced search.

The country specific search mechanism is found at the top of each country page and queries the database by date and category within the selected country and allows the user to view archived news articles. The advanced search mechanism is found on the navigation bar and offers the user a variety of search features.


## Requirements

1. Python 3
2. Flask Web Framework
3. API Keys for the <a href="https://newsapi.org/" target="_blank">News API</a>

## Config File for API Keys

Rename the .env_sample file in the gather directory to .env and add the News API key into that file.  
