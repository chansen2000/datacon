from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Record
from ..email import send_email
from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = Record.query.filter_by(name=form.name.data).first()
        if user is None:

            record=Record(name=form.name.data,address=form.address.data,
                          phone=form.phone.data)
            db.session.add(record)
            session['known'] = False
            #if current_app.config['FLASKY_ADMIN']:
            #    send_email(current_app.config['FLASKY_ADMIN'], 'New User',
            #               'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))
