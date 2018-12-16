from flask import Flask, session, redirect, url_for, escape
from flask import render_template
from flask import request
from flask import Markup
from flask import make_response
from flask import abort
from flask_bootstrap import Bootstrap
from flask import send_file



app = Flask(__name__)
Bootstrap(app)





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': #this block is only entered when the form is submitted
        url = request.form.get('url')
        data = download_video(url)
        return redirect(url_for('download'))

    return '''<form method="POST">
                  Video url to download: <input type="text" name="url"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        return send_file('views.py', attachment_filename='views')
    return '''Confirm Download
<form action="/download" method="post">
        <button type="submit" formmethod="post">Click Me!</button>
        </form>'''



def download_video(url):
    return url[::-1]
