from app import db
from datetime import datetime

ProductTag = db.Table('Product_Tag',
                        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                        db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
                        )
