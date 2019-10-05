from flask import Flask, request, escape, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import app_config
import datetime
import os


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv('FLASK_ENV')]())
    return app