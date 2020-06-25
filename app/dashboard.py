from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from .models import *

dashboard = Blueprint("dashboard", __name__, static_folder="static",
                      template_folder="template")


@dashboard.route('/view')
@login_required
def dashboard_():
    user_book_data = Data.query.filter_by(username=current_user.username)
    return render_template('dashboard.html', name=current_user.username, books=user_book_data)