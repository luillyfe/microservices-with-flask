import json
from flask_sqlalchemy import SQLAlchemy
from db.settings import app

db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    birthday = db.Column(db.Date)
    gender = db.Column(db.String(2))
    lastContact = db.Column(db.DateTime)
    customerLastTimeValue = db.Column(db.Integer, nullable=True)

    def add(_name, _birthday, _gender, _lastContact, _customerLastTimeValue):
        new_customer = Customer(firstName=_name.get("first"), lastName=_name.get("last"), birthday=_birthday,
            gender=_gender, lastContact=_lastContact, customerLastTimeValue=_customerLastTimeValue)
        db.session.add(new_customer)
        db.session.commit()

    def get_all():
        return Customer.query.all()

    def get_by_id(_id):
        return Customer.query.filter_by(id=_id).first()

    def delete(_id):
        _customer = Customer.query.filter_by(id=_id).first()
        db.session.delete(_customer)
        db.session.commit()

    def update(_id, _name):
        _customer = Customer.query.filter_by(id=_id).first()
        _customer["name"] = _name
        db.session.add(_customer)
        db.session.commit()

    def __repr__(self):
        customer_obj = {
            "id": self.id,
            "name": {
                "first": self.firstName,
                "last": self.lastName
            },
            "birthday": self.birthday,
            "gender": self.gender,
            "lastContact": self.lastContact,
            "customerLastTimeValue": self.customerLastTimeValue
        }
        return json.dumps(customer_obj, indent=4, sort_keys=True, default=str)