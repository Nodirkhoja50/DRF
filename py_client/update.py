import requests
endpoint ="http://localhost:8000/api/products/4/update"
data = {
    'title':"this is updated"
}
get_responce = requests.put(endpoint,json=data)
print(get_responce.json())