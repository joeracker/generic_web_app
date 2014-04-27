# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
from random import randint
#from flaskext.mysql import MySQL
#from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup mysql portions
'''
mysql = MySQL()
mysql.init_app(app)
mysql.MYSQL_DATABASE_USER = "generic"
mysql.MYSQL_DATABASE_PASSWORD = "password"
mysql.MYSQL_DATABASE_DB = "generic"
mysql.init_app(app)
'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://generic:password@localhost/generic'
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

@app.route('/users/', methods=['GET'])
def user():
	users = User.query.all()
	#return jsonify(json_list = users)
	return jsonify(users=[i.serialize for i in users])


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    user_type = db.Column(db.String(80), unique=False)

    def __init__(self, username, email, user_type):
        self.username = username
        self.email = email
        self.user_type = user_type

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'username'	: self.username,
           'email'		: self.email,
           'user_type'	: self.user_type
           #'id'         : self.id,
           #'modified_at': dump_datetime(self.modified_at),
           # This is an example how to deal with Many2Many relations
           #'many2many'  : self.serialize_many2many
       }

if __name__ == '__main__':
    app.debug = True
    SERVER_NAME = "0.0.0.0"
    SERVER_PORT = 5000

    app.run(SERVER_NAME, SERVER_PORT)

    #app.run()
