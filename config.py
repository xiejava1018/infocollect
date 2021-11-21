# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
import os
from dotenv import load_dotenv
basedir=os.path.abspath(os.path.dirname(__file__))
flaskenv_path=os.path.join(basedir,'.flaskenv')
env_path=os.path.join(basedir,'.env')
if os.path.exists(flaskenv_path):
    load_dotenv(flaskenv_path)
if os.path.exists(env_path):
    load_dotenv(env_path)

class Config:
    geoLiteDBdir=os.path.join(basedir,'GeoLite2\GeoLite2-City.mmdb')
    flaskenv = os.getenv('FLASK_ENV','development')
    SECRET_KEY=os.getenv('SECRET_KEY','123!@#')
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI')
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI')

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}

if __name__=='__main__':
    conf=Config()
    print(conf.geoLiteDBdir)
    print(conf.SQLALCHEMY_TRACK_MODIFICATIONS)
    print(conf.SQLALCHEMY_DATABASE_URI)
    print(conf.env)