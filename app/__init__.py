import os
import click
from flask import Flask, redirect, request, session, url_for, jsonify
from app.extensions import db, ma
from flask_restful import Resource, Api
from app.config import app_config
from app.models import Category, Order, Payment, Product, Tag, OrderProduct, ProductTag
from app.api.api import test


def create_app():
    app = Flask('shopping', static_url_path='/static')
    app.config.from_object(app_config[os.getenv('FLASK_ENV')])
    register_extensions(app)
    register_api(app)
    register_commands(app)
    register_errors(app)
    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)

def register_api(app):
    api = Api(app)
    api.add_resource(test, '/api')

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return 'ERROR400', 400

    @app.errorhandler(404)
    def page_not_found(e):
        return 'ERROR404', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return 'ERROR500', 500


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        if drop:
            click.confirm(
                'This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')
    @app.cli.command()

    @click.option('--tag', default=10, help='Quantity of tag, default is 10.')
    @click.option('--product', default=10, help='Quantity of product, default is 10.')
    def forge(tag, product):
        from app.fakes import fake_tags, fake_products
        db.drop_all()
        db.create_all()

        click.echo('Generating %d tags' % tag)
        fake_tags(tag)

        click.echo('Generating %d products' % product)
        fake_products(product)