# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    name = StringField(u'姓名', validators=[Required()])
    phone=StringField(u'电话',validators=[Required()])
    address=StringField(u'地址', validators=[Required()])
    submit = SubmitField('Submit')
