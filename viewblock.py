from flask import Flask, render_template, request
import requests
from ast import literal_eval
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  return render_template('index.html')

@app.route("/api/v1/transaction", methods=['GET', 'POST'])
def checkTransaction():
  try:
    params = {
      'X-APIKEY': '38cd0c077fedb10b6c3e45d6c62f32724336b4e39702afe419fe4fc74ff0d8bf',
    }
    address = request.args.get('address')
    r = requests.get(
        'https://api.viewblock.io/v1/zilliqa/addresses/' + address + '/txs',
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
  except:
    noLatestXSGD = "Latest Transaction is not XSGD"
    return render_template('test.html', address=add, verified = noLatestXSGD)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)


