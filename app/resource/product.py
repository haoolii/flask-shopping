from flask_restful import Resource
from flask import request
from app.models.schema.Product import ProductSchema
from app.models.Product import Product
from marshmallow import ValidationError

product_schema = ProductSchema(many=False)

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data

class product(Resource):
    def get(self, productid):
        product = Product.query.get(productid)
        if not product:
            return {
                'message': 'product not exist!'
            }, 403
        return {
            'message': '',
            'product': product_schema.dump(product)
        }
    def put(self, productid):
        try:
            data = product_schema.load(get_param())
            product = Product.query.get(productid)
            product.name = data['name']
            product.price = data['price']
            product.image = data['image']
            product.url = data['url']
            product.description = data['description']
            product.product_type = data['product_type']
            product.category_id = data['category_id']
            product.update()
            return {
                'message': '',
                'product': product_schema.dump(product)
            }
        except ValidationError as error:
            return {
                'message': error.messages
            }, 404
        except Exception as error:
            return {
                'message': 'Exception Error'
            }, 404
    def delete(self, productid):
        try:
            product = Product.query.get(productid)
            product.delete()
            return {
                'message': 'success'
            }
        except Exception as error:
            return {
                'message': 'Exception Error'
            }, 404

class products(Resource):
    def get(self):
        category = request.args.get('category')
        if not category:
            return {
                'message': 'get all products success',
                'products': Product.get_all_products()
            }
        return {
            'message': ('get %s category products success' % category),
            'products': Product.get_products_by_category(category)
        }
    def post(self):
        try:
            data = product_schema.load(get_param())
            product = Product(
                        name=data['name'],
                        price=data['price'],
                        description=data['description'],
                        image=data['image'],
                        product_type=data['product_type'],
                        category_id = data['category_id']
                    )
            product.add()
            return {
                'message': 'create success',
                'product': product.json
            }
        except ValidationError as error:
            return {
                'message': error.messages
            }, 404

