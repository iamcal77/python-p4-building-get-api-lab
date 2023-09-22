# Import necessary modules and classes
from datetime import date
from app import db

# Define the Bakery model
class Bakery(db.Model):
    __tablename__ = 'bakery'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=date.today)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at
        }

# Define the BakedGood model
class BakedGood(db.Model):
    __tablename__ = 'baked_good'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.Date, default=date.today)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'created_at': self.created_at
        }
