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
    publishedAt = db.Column(db.Text)
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))

# Define the us_news data-model
class us_news(db.Model):
    __tablename__ = 'us_news'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
    urlToImage = db.Column(db.String(100))
    publishedAt = db.Column(db.Text)
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))

# Define the au_news data-model
class au_news(db.Model):
    __tablename__ = 'au_news'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
    urlToImage = db.Column(db.String(100))
    publishedAt = db.Column(db.Text)
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))

# Define the ca_news data-model
class ca_news(db.Model):
    __tablename__ = 'ca_news'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
    urlToImage = db.Column(db.String(100))
    publishedAt = db.Column(db.Text)
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))

# Define the nz_news data-model
class nz_news(db.Model):
    __tablename__ = 'nz_news'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
    urlToImage = db.Column(db.String(100))
    publishedAt = db.Column(db.Text)
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))

# Define the gb_news data-model
class gb_news(db.Model):
    __tablename__ = 'gb_news'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100))
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    url = db.Column(db.String(100))
    urlToImage = db.Column(db.String(100))
    publishedAt = db.Column(db.Text)
    content = db.Column(db.String(100))
    news_type = db.Column(db.String(100))