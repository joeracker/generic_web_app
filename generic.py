# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
from random import randint
from flaskext.mysql import MySQL

app = Flask(__name__)

# Setup mysql portions
mysql = MySQL()
mysql.init_app(app)
mysql.MYSQL_DATABASE_USER = "generic"
mysql.MYSQL_DATABASE_PASSWORD = "password"
mysql.MYSQL_DATABASE_DB = "generic"

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random/')
def random_render():
    return render_template('random.html')

@app.route('/random/number')
def random_number():
    #rand_num = random.random()
    return jsonify(result=randint(0,100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    app.debug = True
    SERVER_NAME = "0.0.0.0"
    SERVER_PORT = 5000

    app.run(SERVER_NAME, SERVER_PORT)

    #app.run()
foo