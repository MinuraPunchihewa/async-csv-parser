import os
from urllib.parse import quote


# create the super class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_HOST = os.environ.get('DB_HOST')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_DRIVER = os.environ.get('DB_DRIVER')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    SQLALCHEMY_DATABASE_URI = DB_DRIVER + '://' + DB_USER + ':{}@'.format(quote(DB_PASSWORD)) + DB_HOST + ':' + DB_PORT + '/' + DB_NAME


# create the development config
class DevelopmentConfig(Config):
    DEBUG = True


# create the production config
class ProductionConfig(Config):
    pass


# create the testing config
class TestingConfig(Config):
    pass

