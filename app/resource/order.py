from flask_restful import Resource
from flask import request
from app.models.schema.Order import OrderSchema
from app.models.Order import Order
from app.models.Product import Product
from marshmallow import ValidationError
from flask_jwt_extended import (decode_token, create_access_token)

order_schema = OrderSchema(many=False)

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data

class order(Resource):
    def post(self):
        try:
            data = order_schema.load(get_param())
            product = Product.query.get(data['product_id'])
            if data['receiver_product_type'] not in product.product_type.split(','):
                return {
                    'message': '沒這款貨'
                }, 400
            order = Order(
                        product_id=data['product_id'],
                        amount=data['amount'],
                        receiver_name=data['receiver_name'],
                        receiver_phone=data['receiver_phone'],
                        receiver_addr1=data['receiver_addr1'],
                        receiver_addr2=data['receiver_addr2'],
                        receiver_product_type=data['receiver_product_type'],
                        payment_id = data['payment_id'],
                        recode = data['recode']
                    )
            order.add()
            token = create_access_token(identity = order.id)
            return {
                'message': 'order create success',
                'token': token,
                'order': order.json
            }
        except:
            return {
                'message': 'some errors occur!'
            }, 400
    def get(sef):
        token = request.args.get('token')
        orderId = decode_token(token)['identity']
        order = Order.query.get(orderId)
        return {
            'message': 'get order',
            'order': order.json
        }

class orders(Resource):
    def get(sef):
        return {
            'message': 'get all orders',
            'orders': Order.get_all_orders()
        }