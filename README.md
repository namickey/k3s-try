# k3s-try

memo

## install kubectl
```
# install kubectl for ubuntu
snap install kubectl --classic


# https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

kubectl version --client


# https://qiita.com/hidemaru/items/89c783fec8b402e7bfb5
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

chmod +x ./kubectl
Move the binary in to your PATH.
sudo mv ./kubectl /usr/local/bin/kubectl
```

## install k3s
```
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
 or
curl -sfL https://get.k3s.io | sh -s - server --write-kubeconfig-mode 644 --flannel-backend=ipsec

cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
kubectl get nodes
```

## install argocd
```
https://techstep.hatenablog.com/entry/2021/12/28/130109

# only core
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/core-install.yaml
```

## install argocd cli
```
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
```

## start argocd
```
argocd login --core

argocd version

kubectl config set-context --current --namespace=argocd
cd ~/.kube
sudo cp config /etc/rancher/k3s/k3s.yaml

argocd version

argocd admin dashboard

ssh -L 8081:localhost:8080 user@xx.xx.xx.xx -N

http://localhost:8081
```

## CI

GitHub Actionsを利用したDockerイメージの自動ビルドを試す  
https://tech-lab.sios.jp/archives/29689  

docker docs: Configure CI/CD for your application  
https://matsuand.github.io/docs.docker.jp.onthefly/language/java/configure-ci-cd/  

https://medium.berkayozcan.com/automate-docker-image-builds-for-spring-boot-apps-with-github-actions-3017c684ce99  
https://medium.com/@mamthamalar/ci-with-github-actions-publish-docker-images-de8f1f610fac  
https://www.springcloud.io/post/2022-08/springcloud-github-actions/#gsc.tab=0  
https://spring.pleiades.io/guides/topicals/spring-boot-docker/  

## try kubectl
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
