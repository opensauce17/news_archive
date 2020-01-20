from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CGVC39xyCk8lUmR6DzT_LA'

db = SQLAlchemy(app)

from news.main.routes import main
from news.za.routes import za
from news.us.routes import us
from news.au.routes import au
from news.ca.routes import ca
from news.nz.routes import nz
from news.gb.routes import gb


app.register_blueprint(za)
app.register_blueprint(main)
app.register_blueprint(us)
app.register_blueprint(au)
app.register_blueprint(ca)
app.register_blueprint(nz)
app.register_blueprint(gb)