# database.py
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'books.db')

db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_PATH}'
    db.init_app(app)
    migrate.init_app(app, db)
