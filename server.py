from flask import Flask, jsonify, request
from marshmallow import Schema, fields, pprint

import json

from db import Product, Session

class ProductSchema(Schema):
    title = fields.Str(required=True)
    price_rup = fields.Int(required=True)
    product_image = fields.Str(required=False)
    in_store = fields.Bool(required=False)


app = Flask(__name__)

@app.route('/products/', methods = ['GET', 'POST'])
def products_headle():
    session = Session()

    if request.method =='GET':
        search_query = request.args.get('q')
        products_to_show = session.query(Product)
        if search_query is not None:
            ilike_query = '%%s%' % search_query
            products_to_show = products_to_show.filter(Product.title.ilike(ilike_query))
            # products_to_show = [p for p in PRODUCTS if search_query.lower() in p['title'].lower()]
        is_onli_in_store = 'only_in_store' in request.args

        if is_onli_in_store:
            #  STOP HERE
            products_to_show = products_to_show.filter(Product.in_store = True)

            # products_to_show = [p for p in PRODUCTS if p['in_store']]

        raw_from = request.args.get('from')
        raw_to = request.args.get('to')

        if raw_from and raw_to and raw_from.isdigit() and raw_from.isdigit():
            products_to_show = products_to_show[int(raw_from):int(raw_to)]

        raw_fields = request.args.get('fields')

        if raw_fields:
          fields = raw_fields.split(',')
          products_to_show = [{k:v for (k,v) in p.items() if k in fields} for p in products_to_show]

        return jsonify(products_to_show)
    elif request.method == 'POST':
        request_data = json.loads(request.data.decode('utf-8'))
        if  is_product_data_validate(request_data):
            PRODUCTS.append(request_data)
            return jsonify('ok')
        else:
            response = jsonify('data_error')
            response.status_code = 400
            return response

def is_product_data_validate(product_data):

    errors = ProductSchema.validate(product_data)
    print(errors)
    return not errors

if __name__ =='__main__':

    app.run()
