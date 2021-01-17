from flask import request, Flask, jsonify
import client
import paho.mqtt.client as mqtt
import uuid

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect('localhost', 1883, 10)
mqttc.loop_start()

#オーダー
# for order service
@app.route('/create', methods=['POST'])
def createOrder():
    data = request.get_json()
    no = publishOrder(data)
    totalPrice = client.sum(data)
    return jsonify({
      "no": no,
      "totalPrice": totalPrice,
    })

def publishOrder(data):
    print('pub')
    no = str(uuid.uuid4())[:4].upper()
    value = 'no=' + no + ','
    for k, v in data.items():
        value += k + '=' + v + ','
    mqttc.publish("order", value)
    return no




#支払い
# for pay service
@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    total = 0
    for k, v in data.items():
        total += int(v) * getPrice(k)
    return jsonify({
      "totalPrice": str(total),
    })

def getPrice(key):
    return 101



#受け取り
# for pickup service
pickupSet = set()

@app.route('/add', methods=['POST'])
def addOrder():
    data = request.get_json()
    pickupSet.add(data['no'])
    return jsonify({
      "orders": str(pickupSet),
    })

@app.route('/pickup', methods=['POST'])
def pickup():
    data = request.get_json()
    pickupSet.pop(data['no'])





if __name__ == '__main__':
    app.run()
