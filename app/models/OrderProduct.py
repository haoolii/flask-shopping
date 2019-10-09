from app.extensions import db
from datetime import datetime


OrderProduct = db.Table('OrderProduct',
                        db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
                        db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True)
                        )
