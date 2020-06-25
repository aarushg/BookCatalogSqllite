from . import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired, Length
from wtforms import BooleanField, PasswordField, StringField
from sqlalchemy.dialects.postgresql import JSON


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    registered_on = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    dop = db.Column(db.String(100))
    notes = db.Column(db.String())

    def __init__(self, username, title, author, dop, notes):
        self.title = title
        self.username = username
        self.author = author
        self.dop = dop
        self.notes = notes

class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(
        message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])
