# -*- coding: utf-8 -*-

'''
Using tutorial from http://tech.pro/tutorial/1213/how-to-build-an-api-with-python-and-flask
and http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask (which I like better)
'''

from flask import Flask, jsonify, render_template, request, abort, json
from random import randint
from flask.ext.sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

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

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        if not request.json:
            abort(400)

        # Save to the Database
        user = User(request.json['username'], request.json['email'], request.json['user_type'])
        db.session.add(user)
        db.session.commit()
        return jsonify( {'user': user.serialize, 'URI': request.url + '/' + str(user.id)} ), 201

    elif request.method == 'GET':
		    users = User.query.all()
		    return jsonify(users=[i.serialize for i in users])


@app.route('/users/<int:user_id>', methods=['GET', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        user = User.query.filter_by(id=user_id).first_or_404()
        return jsonify({'user': user.serialize})
    elif request.method == 'PUT':
        return 'not implemented'
    elif request.method == 'DELETE':
        user = User.query.filter_by(id=user_id).first_or_404()
        db.session.delete(user)
        db.session.commit()
        return jsonify( {'DELETE' : 'successful', 'resource': request.url}), 200

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
       """
       Return object data in easily serializeable format
       Handy notes from http://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask

       """
       return dict({
       	   'id'			: self.id,
           'username'	: self.username,
           'email'		: self.email,
           'user_type'	: self.user_type
           #,'URI' : request.url + '/' + str(self.id)
           #'modified_at': dump_datetime(self.modified_at),
           # This is an example how to deal with Many2Many relations
           #'many2many'  : self.serialize_many2many
       })

if __name__ == '__main__':
    app.debug = True
    SERVER_NAME = "0.0.0.0"
    SERVER_PORT = 5000

    app.run(SERVER_NAME, SERVER_PORT, debug=True)
