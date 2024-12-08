import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    from flask_migrate import upgrade
    try:
        upgrade()
    except Exception as e:
        print(f"Ошибка при выполнении миграций: {e}")

from . import views, views
