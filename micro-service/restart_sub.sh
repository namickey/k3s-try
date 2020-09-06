sudo kubectl delete deployment/sub

sleep 2

cd sub
docker build -t namickey/sub-mqtt:1.0 .
cd ../

sleep 2

sudo kubectl create -f sub.yaml
