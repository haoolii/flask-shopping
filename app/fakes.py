from app.models.Tag import Tag
from faker import Faker
from app import db
from app.models.Tag import Tag

fake = Faker()


def fake_tags(count=10):
    for i in range(count):
        tag = Tag(name=fake.word())
        db.session.add(tag)
        db.session.commit()
