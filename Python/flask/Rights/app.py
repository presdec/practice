from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '9658457512645145615asd58436asd458'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/posts.db'
db = SQLAlchemy(app)
metadata = db.MetaData()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"


'''
# authors = db.Table('authors', metadata, autoload=True, autoload_with=engine)
# query = db.select([authors.columns.au_fname, authors.columns.au_lname, 
#                   authors.columns.phone, authors.columns.address, 
#                   authors.columns.city, authors.columns.state, 
#                   authors.columns.zip])
# ResultProxy = connection.execute(query)
# ResultSet = ResultProxy.fetchall()
# print(ResultSet)
# print()
'''

@app.route('/')
def hello():
    pass
