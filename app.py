from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#just for testing purposes. the @cross_origin at this level includes all the more specific api calls
@app.route('/')
@cross_origin()
def home():
    return "Hello to Api"

#create a new store POST api, open store.json take the list in, append it, close it
@app.route('/storePost', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_data = {
        'name': request_data['name'],
        'items': []
    }
    filename = "store.json"
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["stores"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)  
    return request_data

#returns a list of all stores GET api
@app.route('/store')
def get_all_store_name():
    filename = "store.json"
    with open(filename,'r') as file:
        file_data = json.load(file)
        x = jsonify(file_data)
    return jsonify(file_data)

#adds item and price to exising store POST api. if store exists more than once it adds it only to the first found
@app.route('/store/<string:name>/items', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    filename = "store.json"
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    with open(filename,'r+') as file:
        file_data = json.load(file)
        for store in file_data['stores']:
            if store['name'] == name:
                print("MATCH!!")
                store['items'].append(new_item)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)
                print("returning request data")
                return request_data 
    print("returing store not found")
    return jsonify({'message':'store not found'})
    
app.run(port=5000)