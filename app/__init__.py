import os
import click
from flask import Flask, redirect, request, session, url_for, jsonify
from app.extensions import db
from app.config import app_config
from app.models import Category, Order, Payment, Product, Tag, OrderProduct, ProductTag

from app.blueprints.admin import admin_blueprint
from app.blueprints.api import api_blueprint


def create_app():
    app = Flask('shopping', static_url_path='/static')
    app.config.from_object(app_config[os.getenv('FLASK_ENV')])
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    return app


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(api_blueprint, url_prefix='/api')


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