# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class InputForm(FlaskForm):
    name=StringField('域名\IP：',validators=[Required()],render_kw = { 'style':'width:280px;' })
    submit=SubmitField('提交')