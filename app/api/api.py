import os
from flask import request, jsonify
from app.models.Product import Product, ProductSchema
from flask_restful import reqparse, abort, Api, Resource


class test(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='email is required')
    parser.add_argument('password', required=True, help='password is required')

    def get(self):
        return {'hello': 'world'}

    def post(self):
        arg = self.parser.parse_args()

        user = {
            'email': arg['email'],
            'password': arg['password']
        }

        productSchema = ProductSchema()
        errors = productSchema.validate(user)
        if errors:
            return errors

        return user


class tag(Resource):
    def get(self, tagid=False):
        print('?')
        if tagid:
            return {'type': 'tagid: %s ' % tagid}
        productSchema = ProductSchema()
        product_list = Product.query.all()

        res_list = []
        for i in product_list:
            res_list.append(productSchema.dump(i))
        return jsonify(results=res_list)