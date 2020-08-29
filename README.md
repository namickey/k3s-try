# k3s-try

```
curl -sfL https://get.k3s.io | sh -

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
