# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from config import Config
from app import create_app
FLASK_ENV=Config().flaskenv
app = create_app(FLASK_ENV)

if __name__=='__main__':
    app.run()