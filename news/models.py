from news import db

# Define the za_news data-model
class za_news(db.Model):
    __tablename__ = 'za_news'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
    urlToImage = db.Column(db.String(100))
    #publishedAt = db.Column(db.DateTime)
    publishedAt = db.Column(db.Text)
    #publishedAt = db.Column(db.String(100))
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))