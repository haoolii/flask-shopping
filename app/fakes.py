import random
from faker import Faker
from app import db
from app.models.Tag import Tag
from app.models.Product import Product


fake = Faker()


def fake_tags(count=10):
    for i in range(count):
        tag = Tag(name=fake.word())
        db.session.add(tag)
        db.session.commit()

def fake_products(count=10):
    for i in range(count):
        product = Product(
            name=fake.word(),
            price=random.randint(100,9000) ,
            image="https://flask-shopping.herokuapp.com/static/don.jpg",
            url="https://flask-shopping.herokuapp.com/static/don.jpg",
            description=fake.sentence(),
            product_type=fake.word(),
            category_id=random.randint(1,1000)
        )
        db.session.add(product)
        db.session.commit()
