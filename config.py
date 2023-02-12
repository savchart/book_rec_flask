import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DF_PATH = os.path.join(basedir, 'data/df.csv')
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
