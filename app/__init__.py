import os
from flask import Flask, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from config import app_config
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])
db = SQLAlchemy(app)

from app.models import Category, Order, Payment, Product, Tag, OrderProduct, ProductTag

@app.route('/')
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=int(os.getenv('PORT', 8787)))

from app import commands