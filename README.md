# k3s-try

memo

## install
```
curl -sfL https://get.k3s.io | sh -
```

## kubectl
```
sudo k3s kubectl get nodes
sudo k3s kubectl get all -o wide
sudo k3s kubectl apply -f a.yaml
sudo k3s  kubectl expose deployment ad --port=8080 --target-port=80 --type LoadBalancer

sudo ufw allow 22/tcp
sudo ufw allow 6443/tcp
sudo ufw allow 8472/tcp
sudo ufw allow 2379:2380/tcp
sudo ufw allow 10250/tcp
```

```
sudo docker-compose up -d
sudo docker-compose down
sudo docker build -t namickey/flaskpod:1.2 .
sudo docker run namickey/flaskpod:1.2
sudo docker login
sudo docker push namickey/flaskpod:1.2
sudo k3s kubectl create -f flaskpod.yaml
sudo k3s  kubectl expose deployment fd --port=5000 --target-port=5000 --type LoadBalancer

https://dev.classmethod.jp/articles/docker-multi-architecture-image-build/
sudo docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
sudo docker buildx ls
sudo docker buildx create --name mix
sudo docker buildx use mix
sudo docker buildx inspect --bootstrap
sudo docker buildx build --platform linux/amd64,linux/arm/v7 -t namickey/flaskpodmix:latest --push .
sudo k3s kubectl create -f flaskpod.yaml
sudo k3s kubectl expose deployment fd --port=5000 --target-port=5000 --type=LoadBalancer
sudo k3s kubectl get all -o wide
sudo k3s kubectl delete svc fd
sudo k3s kubectl delete deployment fd
sudo k3s kubectl apply -f flaskpod.yaml
sudo k3s kubectl run --image=centos:7 --restart=Never --rm  -i testpod -- curl -s http://fd:5000

master と workerを起動
python check.py
sudo k3s kubectl apply -f flaskpod.yaml

```


https://qiita.com/sky0621/items/beb12145f1b674fe7904
https://qiita.com/Tsu_hao_Zhang/items/7d4f5d62bed584766881

## postgres
```
sudo docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
sudo docker buildx ls
sudo docker buildx create --name mix
sudo docker buildx use mix
sudo docker buildx inspect --bootstrap
sudo docker buildx build --platform linux/amd64,linux/arm/v7 -t namickey/flask-postgres-podmix:latest --push .
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
sudo systemctl disable k3s
sudo systemctl enable k3s
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

## burger
```
python app.py
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/create -d '{"1": "1"}'

```
