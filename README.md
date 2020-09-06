# k3s-try

## install
```
curl -sfL https://get.k3s.io | sh -
```

## hello
```
sudo kubectl get nodes
sudo kubectl get pods
sudo kubectl create -f pod-nginx.yaml
sudo kubectl get pods
sudo kubectl port-forward nginx-pod 8080:80
sudo kubectl delete pods --all
sudo kubectl get pods
sudo kubectl get all

sudo kubectl expose deployment nginx-deployment --port 80 --type LoadBalancer
sudo kubectl describe pods my-pod
sudo kubectl logs my-pod
sudo kubectl delete deployment python-deployment

sudo kubectl exec -it [POD-NAME] -c [CONTAINER-NAME] bash

sudo systemctl status k3s
sudo systemctl stop k3s
sudo systemctl start k3s
```

## micro-service
```
sudo kubectl run mos --image=eclipse-mosquitto --port 1883
sudo kubectl expose pod mos --port=1883 --target-port=1883 --type LoadBalancer
sudo kubectl logs mos
sudo kubectl logs -f mos

pip install paho-mqtt
python sub.py
python pub.py

docker build -t namickey/pub-mqtt:1.0 .
sudo kubectl create -f pub.yaml
sudo kubectl describe pods pub
sudo kubectl delete job pub

/etc/systemd/system/k3s.service
k3s server --docker

docker build -t namickey/sub-mqtt:1.0 .
sudo kubectl create -f sub.yaml
sudo kubectl logs -f job/sub
sudo kubectl exec -it sub-wxpvw bash
sudo kubectl logs sub-wxpvw

command: ["python", "-u", "pub.py"]
```
