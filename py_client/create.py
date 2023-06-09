import requests

data = {
    "title":"this is from mixin!",
    'price':122
}

endpoint ="http://localhost:8000/api/products/"
get_responce = requests.post(endpoint,json=data)
print(get_responce.json())