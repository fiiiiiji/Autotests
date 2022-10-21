from urllib import response
import requests

response = requests.get("https://petstore.swagger.io/v2/pet/999")

print(response.text)