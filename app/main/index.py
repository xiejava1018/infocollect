# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response
from app.main.Forms import InputForm
from app.module.service.ipinfo.getip import checkip, getIPbyDomain
from app.module.service.ipinfo.ipinfo import getipinfo
from app.module.service.whois.whoisinfo import getwhoisinfobychinafu

index_bp=Blueprint('index',__name__)

@index_bp.route('/',methods=['GET','POST'])
def index():
    name = ''
    ipinfos = []
    whois_info = ''
    form = InputForm()
    if form.validate_on_submit():
        name = form.name.data
        if checkip(name):
            ipinfos = getipinfo(name)
        else:
            whois_info = getwhoisinfo(name)
            whois_ip = getIPbyDomain(name)
            if checkip(whois_ip):
                ipinfos = getipinfo(whois_ip)
        form.name.data = ''
    return render_template('index.html',form=form, name=name, ipinfos=ipinfos, whois_info=whois_info)

#@index_bp.route('/getwhois/<domain>')
def getwhoisinfo(domain):
    whois_info=getwhoisinfobychinafu(domain)
    return whois_info