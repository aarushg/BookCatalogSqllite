from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from .models import *


share = Blueprint("share", __name__, static_folder="static",
                  template_folder="templates")

@share.route('/share', methods=['POST'])
@share.route('/share')
def share_():
    if request.method == 'POST':

        shareMail = request.form['shareMail']
        user_book_data = Data.query.filter_by(username=current_user.username)



    #    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    html = render_template('list.html', books=user_book_data)
    subject = "Shared Book List"

    from .email import send_email
    send_email(shareMail, subject, html)


    return render_template('dashboard.html', name=current_user.username, books=user_book_data)