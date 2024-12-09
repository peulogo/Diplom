import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class DevelopementConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
