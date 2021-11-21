# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import Flask
from app.main.index import index_bp
from config import config
from app.exts import db

def create_app(config_name):
    app=Flask(__name__)
    app.register_blueprint(index_bp)
    app.config.from_object(config[config_name])
    db.init_app(app)
    #config[config_name].init_app(app)
    return app
