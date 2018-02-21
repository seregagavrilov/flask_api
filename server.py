from flask import Flask, jsonify, request

import json

from Products import PRODUCTS



app = Flask(__name__)

@app.route('/products/', methods = ['GET', 'POST'])
def products_headle():
    if request.method =='GET':
        search_query = request.args.get('q')
        products_to_show = PRODUCTS
        if search_query is not None:
            products_to_show = [p for p in PRODUCTS if search_query.lower() in p['title'].lower()]
        is_onli_in_store = 'only_in_store' in request.args

        if is_onli_in_store:
            products_to_show = [p for p in PRODUCTS if p['in_store']]

        raw_from = request.args.get('from')
        raw_to = request.args.get('to')

        if raw_from and raw_to:
            products_to_show = products_to_show[int(raw_from):int(raw_to)]

        raw_fields = request.args.get('fields')

        if raw_fields:
          fields = raw_fields.split(',')
          products_to_show = [{k:v for (k,v) in p.items() if k in fields} for p in products_to_show]

        return jsonify(products_to_show)
    elif request.method == 'POST':
        request_data = json.loads(request.data.decode('utf-8'))
        PRODUCTS.append(request_data)
        return jsonify('pk')

if __name__ =='__main__':

    app.run()
