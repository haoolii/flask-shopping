from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from app import create_app
import os

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello!Flask-Shop!'
    
if __name__=="__main__":
    app.run(host=os.getenv('IP', '127.0.0.1'), 
            port=int(os.getenv('PORT', 8787)))