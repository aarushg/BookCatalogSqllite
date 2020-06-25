from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import (login_user, logout_user, login_required)
from werkzeug.security import check_password_hash, generate_password_hash
from .models import *
from .token import generate_confirmation_token, confirm_token
import datetime

auth = Blueprint("auth", __name__, static_folder="static",
                  template_folder="templates")


@auth.route('/login', methods=['GET', 'POST'])
def login_():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                if user.confirmed == True:
                    login_user(user, remember=form.remember.data)
                    return redirect(url_for('dashboard.dashboard_'))
                return '<h1>Please verify your email</h1>'

        return '<h1>Invalid username or password</h1>' 

    return render_template('login.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup_():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data, method='sha256')
        new_user = User(username=form.username.data,
                        email=form.email.data, password=hashed_password, registered_on=datetime.datetime.now(), confirmed=False, confirmed_on=None)
        db.session.add(new_user)
        db.session.commit()

        token = generate_confirmation_token(new_user.email)
        
        confirm_url = url_for('auth.confirm_email', token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        
        from .email import send_email 
        send_email(new_user.email, subject, html)

        login_user(new_user)
        flash('A confirmation email has been sent via email.', 'success')

        return redirect(url_for('auth.login_'))
        # return '<h1>New user has been created!</h1>'

    return render_template('signup.html', form=form)

@auth.route('/logout')
@login_required
def logout_():
    logout_user()
    return redirect(url_for('main.index'))

'''         confirm_url = url_for('user.confirm_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html) '''