# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from app.exts import db

class IPInfo(db.Model):
    __tablename__='ipinfo'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    ip=db.Column(db.String(128))
    country=db.Column(db.String(255))
    region=db.Column(db.String(255))
    city=db.Column(db.String(255))
    org=db.Column(db.String(64))
    isp=db.Column(db.String(64))
    loc=db.Column(db.String(64))
    timezone=db.Column(db.String(64))
    source=db.Column(db.String(64))
    updatetime=db.Column(db.String(64))

    def __repr__(self):
        return '<IPInfo %r,updatetime:%s>' % (self.id,self.updatetime)
        IPInfo.metadata.drop_all()
        IPInfo.metadata.create_all()


class WhoisInfo(db.Model):
    __tablename__ = 'whoisinfo'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    domain_name=db.Column(db.String(255))
    registrar = db.Column(db.String(255))
    registrar_email = db.Column(db.String(128))
    registrar_phone = db.Column(db.String(32))
    registrar_creation_date = db.Column(db.String(32))
    registrar_updated_date = db.Column(db.String(32))
    registrar_expiry_date = db.Column(db.String(32))
    registrar_whois_server = db.Column(db.String(255))
    name_server = db.Column(db.String(255))
    domain_status = db.Column(db.String(512))
    detail= db.Column(db.String(10000))
    source=db.Column(db.String(32))
    updated_time= db.Column(db.String(64))

    def __repr__(self):
        return '<WhoisInfo %r>' % self.id

class QueryLog(db.Model):
    __tablename__ = 'querylog'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    querystr = db.Column(db.String(255))
    query_count=db.Column(db.Integer,default=1)
    query_time=db.Column(db.String(64))

    def __repr__(self):
        return '<QueryLog %r,query_time:%s>' % (self.id,self.query_time)
        QueryLog.metadata.drop_all()
        QueryLog.metadata.create_all()