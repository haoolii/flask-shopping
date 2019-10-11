import random
from faker import Faker
from app import db
from app.models.Tag import Tag
from app.models.Product import Product
from app.models.Category import Category
from app.models.Payment import Payment
import json

fake = Faker()

def mock_category():
    with open('mock.json') as json_file:
        data = json.load(json_file)
        for item in data['category_list']:
            category = Category(name = item['name'])
            db.session.add(category)
            db.session.commit()
        

def mock_payment():
    with open('mock.json') as json_file:
        data = json.load(json_file)
        for item in data['payment_list']:
            payment = Payment(
                pay_type = item['pay_type'],
                fee = item['fee']
                )
            db.session.add(payment)
            db.session.commit()

def mock_products(count=10):
    with open('mock.json') as json_file:
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