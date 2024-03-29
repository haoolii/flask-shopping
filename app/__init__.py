import os
import click
from flask import Flask, redirect, request, session, url_for, jsonify
from app.extensions import db, ma, jwt
from flask_restful import Resource, Api
from app.config import app_config
from flask_cors import CORS

def create_app():
    app = Flask('shopping', static_url_path='/static')
    CORS(app)
    app.config.from_object(app_config[os.getenv('FLASK_ENV')])
    register_extensions(app)
    register_api(app)
    register_commands(app)
    register_errors(app)
    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)


def register_api(app):
    api = Api(app)
    # category api
    from app.resource.category import category, categories
    api.add_resource(categories, '/api/v1/category')
    api.add_resource(category, '/api/v1/category/<string:categoryid>')

    # product api
    from app.resource.product import product, products
    api.add_resource(products, '/api/v1/product')
    api.add_resource(product, '/api/v1/product/<string:productid>')

    # order api
    from app.resource.order import order, orders
    api.add_resource(orders, '/api/v1/orders')
    api.add_resource(order, '/api/v1/order')

    # jwt api
    from app.resource.user import UserRegistration, UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh, AllUsers, SecretResource
    api.add_resource(UserRegistration, '/api/v1/registration')
    api.add_resource(UserLogin, '/api/v1/login')
    api.add_resource(UserLogoutAccess, '/api/v1/logout/access')
    api.add_resource(UserLogoutRefresh, '/api/v1/logout/refresh')
    api.add_resource(TokenRefresh, '/api/v1/token/refresh')
    api.add_resource(AllUsers, '/api/v1/users')
    api.add_resource(SecretResource, '/api/v1/secret')


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
    def mock():
        from app.mocks import mock_category, mock_payment, mock_products, mock_orders
        db.drop_all()
        db.create_all()

        click.echo('Mocking Category')
        mock_category()

        click.echo('Mocking Payment')
        mock_payment()

        click.echo('Mocking product')
        mock_products()

        click.echo('Mocking Order')
        mock_orders()