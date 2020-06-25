from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dikqfafmdzjuob:15ab173dbf7181ce7330e50a426f4e946168ba3fd478ca8f5d958bc3c59e992e@ec2-35-172-73-125.compute-1.amazonaws.com:5432/df17nggg4a577h'
db = SQLAlchemy(app)

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

db.create_all()
