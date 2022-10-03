from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sql'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    db.init_app(app)
    # D4 Basic Auth admin = Admin(app, name="DB CONF")
    admin = Admin(app, name="DB CONF")
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .Other import other
    app.register_blueprint(other)
    from .database import Glissades, Patinoire, Piscines
    # D3
    admin.add_view(ModelView(Glissades, db.session))
    admin.add_view(ModelView(Piscines, db.session))

    return app
