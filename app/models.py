from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class DrinkType(db.Model):
    __tablename__ = 'drink_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def toJSON(self):
        return {
        'id' : self.id,
        'name' : self.name,
        'created_at' : self.created_at
        }

class Drink(db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key=True)
    drinktype_id = db.Column(db.Integer, db.ForeignKey('drink_types.id'), nullable=False)
    note = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def toJSON(self):
        return {
        'id' : self.id,
        'drink_type_id' : self.drinktype_id,
        'note' : self.note,
        'created_at' : self.created_at
        }