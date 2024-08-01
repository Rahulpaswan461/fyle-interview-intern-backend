import os
from dotenv import load_dotenv

load_dotenv() 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DB_SQLALCHEMY_DATABASE_URI = os.environ.get('DB_SQLALCHEMY_DATABASE_URI ')  or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DB_SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' 
    DEBUG = True

class ProductionConfig(Config):
    DB_SQLALCHEMY_DATABASE_URI = os.environ.get('sqlite:///site.db') 
    DEBUG = False

config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY
