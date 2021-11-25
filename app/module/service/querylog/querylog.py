# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from app.exts import db
from app.module.models.dbmodels import QueryLog

def getQueryLog(count):
    return QueryLog.query.order_by(QueryLog.id.desc()).limit(5)

def addQueryLog(querystr):
    querylog =QueryLog.query.filter_by(querystr=querystr).first()
    if querylog:
        querylog.query_count=querylog.query_count+1
    else:
        querylog=QueryLog()
        querylog.querystr=querystr
    db.session.add(querylog)
    db.session.commit()