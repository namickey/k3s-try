from flask import Flask, jsonify, request
import time

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  #time.sleep(1)
  x = request.headers.get("X-Forwarded-For")
  if x:
      print(x)
  return jsonify({
    "message": "テスト!!"
  })

if __name__ == '__main__':
  app.run()
