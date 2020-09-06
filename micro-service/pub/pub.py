#encoding: utf-8
import paho.mqtt.client as mqtt
import time

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect('mos', 1883, 60)
mqttc.loop_start()
mqttc.publish("topic1", "test1")
time.sleep(1)
mqttc.disconnect()
time.sleep(1)
