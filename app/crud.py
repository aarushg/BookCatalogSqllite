from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from .models import *

crud = Blueprint("crud", __name__, static_folder="static",
                      template_folder="template")


@crud.route('/delete/<int:id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Book Deleted Successfully")

    return redirect(url_for('dashboard.dashboard_'))

@crud.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':

        username = request.form['uName']
        title = request.form['title']
        author = request.form['author']
        dop = request.form['dop']
        notes = request.form['notes']

        my_data = Data(username, title, author, dop, notes)
        db.session.add(my_data)
        db.session.commit()

        flash("Book Inserted Successfully")

        return redirect(url_for('dashboard.dashboard_'))

@crud.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.title = request.form['title']
        my_data.author = request.form['author']
        my_data.dop = request.form['dop']
        my_data.notes = request.form['notes']

        db.session.commit()
        flash("Book Updated Successfully")

        return redirect(url_for('dashboard.dashboard_'))


