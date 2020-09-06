sudo kubectl delete job/pub

sleep 2

cd pub
docker build -t namickey/pub-mqtt:1.0 .
cd ../

sleep 2

sudo kubectl create -f pub.yaml
