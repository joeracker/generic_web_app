# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
#    return "hello worlds"

if __name__ == '__main__':
    app.debug = True
    SERVER_NAME = "0.0.0.0"
    SERVER_PORT = 5000

    app.run(SERVER_NAME, SERVER_PORT)

    #app.run()
foo