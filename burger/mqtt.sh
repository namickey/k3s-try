sudo kubectl create -f pod-mqtt.yaml

sleep 5

sudo kubectl create -f svc-mqtt.yaml
