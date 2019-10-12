from app.extensions import db
from passlib.hash import pbkdf2_sha256 as sha256

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    @property
    def json(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.create_at = datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
            return cls.query.filter_by(username = username).first()

    @classmethod
    def return_all(cls):
        return list(i.json for i in cls.query.all())

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return '{} row(s) deleted'.format(num_rows_deleted)
        except:
            return 'Something went wrong'

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)