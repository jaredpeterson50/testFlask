from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]


"""just for testing purposes. the @cross_origin at this level includes all the more specific api calls"""
@app.route('/')
@cross_origin()
def home():
    return "Hello to Api"

"""create a new store POST api"""
@app.route('/storePost', methods=['POST'])
def create_store():
    
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return request_data

"""returns a list of all stores GET api"""
@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})

"""adds item and price to exising store POST api. if store exists more than once it adds it only to the first found"""
@app.route('/store/<string:name>/items', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

app.run(port=5000)