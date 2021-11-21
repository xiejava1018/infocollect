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
    id = db.Column(db.Integer, primary_key=True)
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
        return '<IPInfo %r>' % self.id

class WhoisInfo(db.Model):
    __tablename__ = 'whoisinfo'
    id = db.Column(db.Integer, primary_key=True)
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
        return '<IPInfo %r>' % self.id