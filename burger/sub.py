#encoding: utf-8
import paho.mqtt.client as mqtt
import client

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))
    mqttc.subscribe("order")

# for pickup service
def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    data = {}
    data['no'] = str(msg.payload).split(',')[0].split('=')[1]
    orders = client.add(data)
    print(orders)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect('localhost', 1883, 10)
mqttc.loop_forever()
