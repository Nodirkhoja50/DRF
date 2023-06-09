import requests
from getpass import getpass
auth_point = "http://localhost:8000/api/auth"
username = input('What is your username\n')
password = getpass('What is your password')
data = {
    'username':username,
    'password':password

}
auth_responce = requests.post(auth_point,json=data)#this is going to be token generate
print(auth_responce.json())

if auth_responce.status_code == 200:
    token = auth_responce.json()['token']
    headers = {
        "Authorization": f'Bearer {token}'
    }



    endpoint ="http://localhost:8000/api/products/"
    get_responce = requests.get(endpoint,headers=headers)
    print(get_responce.json())
