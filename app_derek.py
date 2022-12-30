import yaml
import glob
import pprint
from flask import Flask, request, jsonify, render_template, abort, redirect, url_for

app = Flask(__name__)
print(__name__)

with open('./envvars.yml', 'r') as f:
    envVars = yaml.safe_load(f.read())

@app.route('/')
def test():
    return "Dereks API"

@app.route('/envVars')
def test2():
    return(jsonify({'wtf': 'it worked'}))

@app.route('/pnp-device-data', methods=['POST'])
def process_device_data():
    data = request.json
    print(data)
    print(request.data)
    return(jsonify({'wtf': 'it worked'}))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
"""
Postman Request:
Header:
Content-Type: application/json
Body:
{"cdp-neighbors": [{"device-name": "RS1_EDGSW1.spo.compunetdemo.com",
                    "local-intf-name": "GigabitEthernet1/0/23",
                    "port-id": "GigabitEthernet1/0/24"},
                   {"device-name": "ISR_SPOKE1.SPO.COMPUNETDEMO.COM",
                    "local-intf-name": "GigabitEthernet1/0/24",
                    "port-id": "GigabitEthernet0/0/0"}],
 "device-type": "switch",
 "device-id": "FJC2330S0RJ"
 "software": {"rommon-version": "IOS-XE ROMMON", "software-version": "17.3.4"},
 "switches": {1: {"part-no": "C9300-24P",
                  "serial-no": "FJC2330S0RJ",
                  "version": "V02"}}}
"""
