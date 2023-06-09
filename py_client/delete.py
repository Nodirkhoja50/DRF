import requests 
product_id = input('please enter id:')
try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not valid')
if product_id:
    endpoint =f"http://localhost:8000/api/products/{product_id}/delete"
get_responce = requests.delete(endpoint)
print(get_responce.status_code,get_responce.status_code==204)