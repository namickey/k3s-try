sudo k3s kubectl create -f flask-deployment.yaml
sleep 5
sudo k3s kubectl create -f flask-service.yaml
