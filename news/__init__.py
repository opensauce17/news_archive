from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CGVC39xyCk8lUmR6DzT_LA'

db = SQLAlchemy(app)

from news.za.routes import za
from news.main.routes import main

app.register_blueprint(za)
app.register_blueprint(main)