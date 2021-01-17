import json
import urllib.request

# for pay service
def sum(data):
    url = 'http://localhost:5000/sum'
    headers = {
        'Content-Type': 'application/json',
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = json.load(res)
        return body['totalPrice']

# for pickup service
def add(data):
    url = 'http://localhost:5000/add'
    headers = {
        'Content-Type': 'application/json',
    }
    print(data)
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = json.load(res)
        return body['orders']
