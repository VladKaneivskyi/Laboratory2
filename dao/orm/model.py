from datetime import datetime as dt

from flask import Flask, make_response, request, render_template
from flask_sqlalchemy import SQLAlchemy
#from forms import UserForm, FileForm, DocumentationForm, LanguageForm


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vlad16tank@localhost/NoSQL'
db = SQLAlchemy(app)

class Store_Have_Goods(db.Model):
    __tablename__  = 'store_have_goods'
    good_id_fk = db.Column(db.Integer, db.ForeignKey('goods.good_id'), primary_key=True)
    store_id_fk = db.Column(db.Integer, db.ForeignKey('store.store_id'), primary_key=True)

class Characteristic(db.Model):

    __tablename__ = 'characteristic'
    charac_name = db.Column(db.String(20), primary_key=True)
    charac_description= db.Column(db.String(100),primary_key=True)
    c_good_id_fk = db.Column(db.Integer, db.ForeignKey('goods.good_id'))


class Goods(db.Model):

    __tablename__ = 'goods'
    good_id = db.Column(db.Integer, primary_key=True)
    good_name = db.Column(db.String(45))
    good_model = db.Column(db.String(100))

    store_id_fk = db.relationship("Store", secondary="store_have_goods")
    results = db.relationship("Result")
    characters = db.relationship("Characteristic")

class Result(db.Model):

    __tablename__ = 'result'

    result_id = db.Column(db.Integer, primary_key=True)
    r_good_id_fk = db.Column(db.Integer, db.ForeignKey('goods.good_id'))


class Store(db.Model):

    __tablename__ = 'store'
    store_id = db.Column(db.Integer, primary_key=True)
    store_name= db.Column(db.String(20), unique=True, nullable=False)
    store_link = db.Column(db.String(40), unique=True)
    good_id_store_fk = db.relationship("Goods", secondary="store_have_goods")

db.create_all()


if __name__ == "__main__":
    app.run()