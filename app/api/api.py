import os
from app import db
from flask import request, jsonify
from app.models.Product import Product, ProductSchema
from app.models.Category import Category
from flask_restful import reqparse, abort, Api, Resource
from marshmallow import ValidationError
from datetime import datetime

class product(Resource):
    def get(self, productid=False):
        try:
            product = Product.query.get(productid)
            return product.serialize, 200
        except Exception as e:
            return {"reason": repr(e)}, 404
    def put(self, productid=False):
        try:
            product = Product.query.get(productid)
            data = request.get_json()
            category = Category.query.filter_by(name=data['category']).first()
            if category:
                product.name = data['name']
                product.price = data['price']
                product.image = data['image']
                product.url = data['url']
                product.description = data['description']
                product.product_type = data['product_type']
                product.category = category
                product.create_at = datetime.utcnow()
                db.session.commit()
                return product.serialize
            else:
                raise Exception('category is not exist')
        except Exception as e:
            return {"reason": repr(e)}, 404

class products(Resource):
    def get(self):
        try:
            if request.args.get('category'):
                category = Category.query.filter_by(name=request.args.get('category')).first()
                return jsonify(products=[i.serialize for i in Product.query.filter_by(category_id=category.id).all()])
            return jsonify(products=[i.serialize for i in Product.query.all()])
        except Exception as e:
            return {"reason": repr(e)}, 404
    def post(self):
        try:
            data = request.get_json()
            category = Category.query.filter_by(name=data['category']).first()
            if category:
                product = Product(
                        name=data['name'],
                        price=data['price'],
                        description=data['description'],
                        image=data['image'],
                        product_type=data['product_type'],
                        category = category
                    )
                db.session.add(product)
                db.session.commit()
                return product.serialize
            else:
                raise Exception('category is not exist')
        except Exception as e:
            return {"reason": repr(e)}, 404