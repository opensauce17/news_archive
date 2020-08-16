#from .. import global_search

# @app.template_filter()
def strftime(date, format):
    date = x.publishedAt.replace('T', " ").replace('Z', "")
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return date.strftime("%m/%d/%Y")

# app.filters['strftime'] = strftime