#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask import Flask, jsonify
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def get_bakeries():
    # Assuming you have a list of bakery objects, you can jsonify them
    bakeries = [{"id": 1, "name": "Bakery 1"}, {"id": 2, "name": "Bakery 2"}]
    return jsonify(bakeries)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    return ''

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    return ''

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    return ''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
