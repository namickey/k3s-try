from flask import Flask, jsonify, request
import time
import datetime
import hashlib

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

code = ''

@app.route('/')
def index():
  return jsonify({
    "message": "hello"
  })

@app.route('/hash')
def createHash():
  global code
  code = hashlib.sha256(str(datetime.datetime.now()).encode()).hexdigest()[:4].upper()
  return jsonify({
    "code": code
  })

@app.route('/auth/<value>')
def auth(value):
  print(code)
  if code == value.upper():
    return jsonify({
      "result": 'success'
    })
  else:
    return jsonify({
      "result": 'error'
    })

if __name__ == '__main__':
  app.run()

