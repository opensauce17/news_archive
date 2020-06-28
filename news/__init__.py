from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_mail import Mail

app = Flask(__name__)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CGVC39xyCk8lUmR6DzT_LA'
app.config['CFR_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = True
app.config.from_pyfile('../mail.cfg')
app.config['USER_SEND_PASSWORD_CHANGED_EMAIL'] = False
app.config['USER_SEND_REGISTERED_EMAIL'] = True
app.config['USER_SEND_USERNAME_CHANGED_EMAIL'] = False
app.config['USER_APP_NAME'] = 'The World News Archive'

db = SQLAlchemy(app)
mail = Mail(app)


from news.models import User
from news.main.routes import main
from news.search.routes import global_search
from news.za.routes import za
from news.us.routes import us
from news.au.routes import au
from news.ca.routes import ca
from news.nz.routes import nz
from news.gb.routes import gb

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

app.register_blueprint(za)
app.register_blueprint(main)
app.register_blueprint(us)
app.register_blueprint(au)
app.register_blueprint(ca)
app.register_blueprint(nz)
app.register_blueprint(gb)
app.register_blueprint(global_search)