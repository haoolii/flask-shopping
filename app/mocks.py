import random
from app import db
from app.models.Product import Product
from app.models.Category import Category
from app.models.Payment import Payment
from app.models.Order import Order
import json

def mock_category():
    with open('mock.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        for item in data['category_list']:
            category = Category(name = item['name'])
            db.session.add(category)
            db.session.commit()
        

def mock_payment():
    with open('mock.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        for item in data['payment_list']:
            payment = Payment(
                pay_type = item['pay_type'],
                fee = item['fee']
                )
            db.session.add(payment)
            db.session.commit()

def mock_products():
    with open('mock.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        for item in data['product_list']:
            category = Category.query.filter_by(name=item['category']).first()
            product = Product(
                name=item['name'],
                price=item['price'],
                description=item['description'],
                image=item['image'],
                product_type=item['product_type'],
                category = category
            )
            db.session.add(product)
            db.session.commit()

def mock_orders():
    with open('mock.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        for item in data['order_list']:
            product = Product.query.get(item['product_id'])
            payment = Payment.query.get(item['payment_id'])
            order = Order(
                product = product,
                amount = item['amount'],
                receiver_name = item['receiver_name'],
                receiver_phone = item['receiver_phone'],
                receiver_addr1 = item['receiver_addr1'],
                receiver_addr2 = item['receiver_addr2'],
                payment = payment
            )
            db.session.add(product)
            db.session.commit()