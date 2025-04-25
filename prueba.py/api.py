import requests

url = 'https://opentdb.com/api.php?amount=10&category=19&difficulty=medium&type=multiple&encode=url3986'
req = requests.get(url)

if req.status_code == 200:
    data=req.json()

    print("peticion exitosa")
    print('data:', data)
else:
    print("peticion erronea", req.text)    





