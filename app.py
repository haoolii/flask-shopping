import os
from flask import Flask, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from config import app_config
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])
db = SQLAlchemy(app)

app.secret_key='8787'

@app.route('/')
def hello():
    return 'hello'
    
@app.route('/do-something')
def do_something():
    # do something
    # return redirect(url_for('hello'))
    # return redirect(request.referrer)
    return redirect(request.referrer or url_for('hello'))

@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something</a>' % url_for('do_something')

@app.route('/bar')
def bar():
    return '<h1>Bar page</h1><a href="%s">Do something </a>' % url_for('do_something')
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 8787)))
