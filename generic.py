# -*- coding: utf-8 -*-

'''
Using tutorial from http://tech.pro/tutorial/1213/how-to-build-an-api-with-python-and-flask
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

'''
# Example to help with json headaches
# http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'task': make_public_task(task) } ), 201
'''

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'POST':
        if not request.json:
            abort(400)

        user = {
           'username' : request.json['username'],
           'email'    : request.json['email'],
           'user_type'  : request.json['user_type']
        }
        #json_data = request.json()
        #user_json = jsonify(request.get_json(force=True))
        return jsonify( {'user': user} ), 201
        #return user_json['username']
        

        # Save to the Database
        #user = User('bill2', 'bill2@mejoe.com', 'admin')
        #db.session.add(user)
        #db.session.commit()


    elif request.method == 'GET':
		    users = User.query.all()
		    return jsonify(users=[i.serialize for i in users])

@app.route('/users/<id>')
def user(id):
    user = User.query.filter_by(id=id).first_or_404()
    return jsonify(user=user)


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
       return {
       	   'id'			: self.id,
           'username'	: self.username,
           'email'		: self.email,
           'user_type'	: self.user_type
           #'modified_at': dump_datetime(self.modified_at),
           # This is an example how to deal with Many2Many relations
           #'many2many'  : self.serialize_many2many
       }

if __name__ == '__main__':
    app.debug = True
    SERVER_NAME = "0.0.0.0"
    SERVER_PORT = 5000

    app.run(SERVER_NAME, SERVER_PORT, debug=True)
