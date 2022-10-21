from urllib import response
import requests

response = requests.get("https://petstore.swagger.io/v2/pet/999")

print(response.status_code)

if response.status_code == 200:
    print("ok")
else:
    print("Not.ok")