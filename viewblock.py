from flask import Flask, render_template
import requests
from ast import literal_eval
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  params = {
    'X-APIKEY': '38cd0c077fedb10b6c3e45d6c62f32724336b4e39702afe419fe4fc74ff0d8bf',
  }
  r = requests.get(
      'https://api.viewblock.io/v1/zilliqa/addresses/zil193xq8gz97fpf6tr5v9tz4r4uef6k295umzuaq7/txs',
      headers=params)

  add = r.json()
  hashvalue = add[0]['hash']
  receiptSuccess = add[0]['receiptSuccess']

  data = literal_eval(add[0]['data'])
  param = data['params']
  XSGDvalue = param[1]['value']
  actualXSGD = float(XSGDvalue) / 1000000.0

  event = add[0]['events']
  verifyXSGD = event[0]['address']
  transferSuccess = event[0]['name']

  finalParam = event[0]['params']
  senderAdd = finalParam['sender']
  merchantAdd = finalParam['recipient']

  return render_template('test.html', address=add, hash=hashvalue, XSGD = actualXSGD, verified = verifyXSGD, transferSuccess = transferSuccess, senderAdd = senderAdd, merchantAdd = merchantAdd)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)