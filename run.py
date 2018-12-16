from flask import Flask, session, redirect, url_for, escape
from flask import render_template
from flask import request
from flask import Markup
from flask import make_response
from flask import abort
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
